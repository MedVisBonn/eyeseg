import logging
import click

logger = logging.getLogger("eyeseg.layers")


@click.command()
@click.option(
    "--drusen_threshold",
    "-t",
    type=click.INT,
    default=2,
    help="Minimum height for drusen to be included",
)
@click.argument("model_id", type=click.STRING, default="2c41ukad")
@click.pass_context
def segment(ctx: click.Context, model_id, drusen_threshold):
    """Predict OCT layers

    \b
    MODEL_ID: Specifies the model
        Pretrained models:
            Spectralis:
                2c41ukad: 3 classes (BM, RPE, EZ) - (Default)
            Bioptigen:
                3avqygsi: 3 classes (BM, RPE, ILM)
    \f
    """
    # Delay imports for faster CLI
    from importlib import resources

    import eyepy as ep
    from tqdm import tqdm

    from eyeseg.models import weights as weights_resources
    from eyeseg.scripts.utils import find_volumes
    from eyeseg.models.utils import get_layers

    input_path = ctx.obj["input_path"]
    output_path = ctx.obj["output_path"]

    devices = {"2c41ukad": "spectralis", "3avqygsi": "bioptigen"}

    # Check if specified model is available
    if not model_id in list(resources.contents(weights_resources)):
        msg = f"A model with ID {model_id} is not available. Check 'eyeseg layers --help' for available models."
        logger.error(msg)
        raise ValueError(msg)

    # Find volumes
    volumes = find_volumes(input_path)

    data_readers = {
        "vol": ep.import_heyex_vol,
        "xml": ep.import_heyex_xml,
        "duke": ep.import_duke_mat,
    }  # "eye": ep.EyeVolume.load}
    # Predict layers and save
    for datatype, volumes in volumes.items():
        for path in tqdm(
                volumes,
                desc="Volumes: ",
                position=0,
                leave=True,
        ):
            # Load data
            logger.debug(f"Reading data {path}")
            data = data_readers[datatype](path)
            if "age" in data.meta:
                # drop age
                data.meta.pop("age")

            # Predict layers
            if data.shape[1] > 512:
                logger.error(
                    f"{path.name}: Bscans are only supported up to a height of 512 pixels"
                )
                raise click.Abort
            logger.debug("Predicting layers")
            data = get_layers(data, model_id, device=devices[model_id])
            # Save predicted layers
            output_dir = output_path / path.relative_to(input_path).parent
            output_dir.mkdir(parents=True, exist_ok=True)

            rpe_name = f"RPE_{model_id}"
            bm_name = f"BM_{model_id}"
            logger.debug("Predicting drusen")
            drusen = ep.drusen(
                data.layers[rpe_name],
                data.layers[bm_name],
                data.shape,
                minimum_height=drusen_threshold,
            )
            data.add_pixel_annotation(drusen, name="drusen")

            logger.debug("Saving data")
            data.save(output_dir / (path.name + ".eye"))

    click.echo(
        "\nComputed layers and drusen are saved. You can now use the 'quantify', 'plot-enface' and 'plot-bscans' commands"
    )
