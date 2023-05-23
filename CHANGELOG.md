# Changelog

<!--next-version-placeholder-->

## v0.1.0 (2023-05-23)
### Feature
* **eyeseg:** Add Bioptigen model ([`8b99881`](https://github.com/MedVisBonn/eyeseg/commit/8b99881ea91a9164515156447e726f9c7d4ff7e4))
* **eyeseg:** Commit latest changes ([`7c394e9`](https://github.com/MedVisBonn/eyeseg/commit/7c394e9c6bb02a45b841ad3a8271b9959d73f623))
* **Dockerfile:** Update to tensorflow 2.9.1 and set WORKDIR to /home/data by default ([`2709a68`](https://github.com/MedVisBonn/eyeseg/commit/2709a689e303cb5b86982fbd14d01b81921dddd8))
* **eyeseg:** Add train command to train model ([`1a86c2c`](https://github.com/MedVisBonn/eyeseg/commit/1a86c2c37cbdb6dd1a8129206ced6fd2246ae433))
* **scripts:** Separate drusen quantification from drusen computation; add plotting of overview and B-scans ([`3d8aa8e`](https://github.com/MedVisBonn/eyeseg/commit/3d8aa8ef1b31812aedf409a5cca18658beac36c7))
* **scripts:** Predict layers, compute drusen and quantify drusen with user defined grid ([`bec8d82`](https://github.com/MedVisBonn/eyeseg/commit/bec8d8245453acb137ece8e8d830fbd0b34a4191))

### Fix
* **pyproject.toml:** Update eyepie to 0.6.3 ([`1e065a2`](https://github.com/MedVisBonn/eyeseg/commit/1e065a23bdf0d4aae5666c0b485cead1a4ceed29))
* **quantify.py:** Add number of B-scans and correct volume name in results ([`d399227`](https://github.com/MedVisBonn/eyeseg/commit/d3992278fa20499eadf1b4bdff4ee29d8654445f))
* **plot-bscans:** Specify any folder in the input folder hierarchy to plot bscans for all contained volumes ([`3cf6ac1`](https://github.com/MedVisBonn/eyeseg/commit/3cf6ac1ceeb907d400a91208562ea47c781caae0))
* **scripts:** Keep folder structure of input for processed folder ([`bb6bcef`](https://github.com/MedVisBonn/eyeseg/commit/bb6bceff501638e5ab5251a4476f4b33f2104ac0))
* **plot_bscans.py:** Use all volumes if none are specified ([`c76b306`](https://github.com/MedVisBonn/eyeseg/commit/c76b306656d48c50cb6546ff98e1404cddea59d3))
* **scripts:** Fixed output_path overwrite and improve logging ([`d919cc1`](https://github.com/MedVisBonn/eyeseg/commit/d919cc1dee377998752168d30c89e9752a4a988d))
* **scripts:** Fix missing context for drusen command and missing output folder ([`e82e4b9`](https://github.com/MedVisBonn/eyeseg/commit/e82e4b95339d19fb7fc669564cd322c1f22ec13b))

### Breaking
*  ([`2341908`](https://github.com/MedVisBonn/eyeseg/commit/23419085e611e5ea13f68b94bedc654ce00d84d7))
*  ([`239c660`](https://github.com/MedVisBonn/eyeseg/commit/239c660729d76a7e8f3a27bd4f1f241d07e0dd72))

### Documentation
* **README.md:** Remove image download note - use dockerhub instead ([`094cca0`](https://github.com/MedVisBonn/eyeseg/commit/094cca0029cd8b270e99112b778d0bb0aed528cd))
* **scripts:** Add logging and informative messages to the octseg application ([`9c36c91`](https://github.com/MedVisBonn/eyeseg/commit/9c36c91d32ee331cb41f6cdaf878d7c8cc45b2b6))
* **README.md:** Complete the documentation for the current functionalities ([`5f3b17c`](https://github.com/MedVisBonn/eyeseg/commit/5f3b17cc5f0798bdc314224f9205c9da16f88cd2))
* **README.md:** Add development documentation ([`f84e9d5`](https://github.com/MedVisBonn/eyeseg/commit/f84e9d5a294c99aeb4921417aba4940c5f20c360))
