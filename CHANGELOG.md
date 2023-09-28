# CHANGELOG



## v1.0.2 (2023-09-28)

### Fix

* fix(pyproject.toml): downgrade to tensorflow 2.11 ([`81ca68a`](https://github.com/MedVisBonn/eyeseg/commit/81ca68a190480263112bdb50533d26302af2ef64))


## v1.0.1 (2023-09-27)

### Build

* build(poetry.lock): update dependencies ([`08abc52`](https://github.com/MedVisBonn/eyeseg/commit/08abc52f2c0ab47a3011474aa48281aa2ff7d87a))

### Ci

* ci(PythonSematicRelease): update python semantic release to v8 ([`2a50002`](https://github.com/MedVisBonn/eyeseg/commit/2a5000272cb87aaff4d263c07351c0fa39d4f34b))

### Documentation

* docs(README.md): add small clarification on what to expect when using the docker image ([`6d6df66`](https://github.com/MedVisBonn/eyeseg/commit/6d6df664c2c78ee7e270b91d173b45db032e2475))

* docs(README.md): fixes typo and docker image version ([`1a4d631`](https://github.com/MedVisBonn/eyeseg/commit/1a4d631e9f530b7c603321332c250f7e62c9f208))

* docs(README.md): add PyPI badge and mention eyepy fory for loading the results ([`771a38f`](https://github.com/MedVisBonn/eyeseg/commit/771a38fd998e832410456db13b0a775d39212838))

### Fix

* fix(segment.py): fix bug where existing layers are used for drusen computation instead of predicted ([`15d0114`](https://github.com/MedVisBonn/eyeseg/commit/15d0114656622b8fa462d9db0d29a405dfe3ce53))


## v1.0.0 (2023-05-23)

### Breaking

* fix(pyproject.toml): switch to major versioning

BREAKING CHANGE: ([`139d462`](https://github.com/MedVisBonn/eyeseg/commit/139d46267d80d9b8c1a7f6f9309bd8cf5e21a48c))

### Documentation

* docs(README.md;-CITATION.cff): add prefered citation, change from eyeseg to eyesegpy because of availability ([`7d638c0`](https://github.com/MedVisBonn/eyeseg/commit/7d638c03d95a8aac162034ba228a9464aebf821b))

* docs(README): add bibtex reference ([`feead26`](https://github.com/MedVisBonn/eyeseg/commit/feead26cb7c3e63a5c19fb01bbd805584516bcf0))

### Fix

* fix(pyproject.toml;-CITATION.cff): fix versioning ([`ca4dbab`](https://github.com/MedVisBonn/eyeseg/commit/ca4dbab76b30c50b35c1333d40fa7198517a7205))


## v0.1.0 (2023-05-23)

### Breaking

* refactor(eyeseg): refactor, cleanup and document eyeseg

BREAKING CHANGE: ([`2341908`](https://github.com/MedVisBonn/eyeseg/commit/23419085e611e5ea13f68b94bedc654ce00d84d7))

* refactor(eyeseg): work with .eye files for storing results instead of pickel

BREAKING CHANGE: ([`239c660`](https://github.com/MedVisBonn/eyeseg/commit/239c660729d76a7e8f3a27bd4f1f241d07e0dd72))

### Build

* build(docker/scripts): add instructions on how to build and use a docker image for this package ([`c25e805`](https://github.com/MedVisBonn/eyeseg/commit/c25e8059e7b5fac346b0190e29d692a19ad1ca48))

* build: introduce semver and automatic publishing ([`8109603`](https://github.com/MedVisBonn/eyeseg/commit/810960346c67da15236c6a1e8d2d0a9bea6e2a62))

### Ci

* ci(eyeseg): fix versioning ([`11a30d0`](https://github.com/MedVisBonn/eyeseg/commit/11a30d02fdeb17adb75e080feb7f3bab9c2f862c))

* ci(ci.yaml): fix repository check ([`93483c3`](https://github.com/MedVisBonn/eyeseg/commit/93483c3e94e17c5fc87867ec988dfed9f7b3cd24))

### Documentation

* docs(README.md): Remove image download note - use dockerhub instead ([`094cca0`](https://github.com/MedVisBonn/eyeseg/commit/094cca0029cd8b270e99112b778d0bb0aed528cd))

* docs(scripts): add logging and informative messages to the octseg application ([`9c36c91`](https://github.com/MedVisBonn/eyeseg/commit/9c36c91d32ee331cb41f6cdaf878d7c8cc45b2b6))

* docs(README.md): complete the documentation for the current functionalities ([`5f3b17c`](https://github.com/MedVisBonn/eyeseg/commit/5f3b17cc5f0798bdc314224f9205c9da16f88cd2))

* docs(README.md): add development documentation ([`f84e9d5`](https://github.com/MedVisBonn/eyeseg/commit/f84e9d5a294c99aeb4921417aba4940c5f20c360))

### Feature

* feat(eyeseg): add Bioptigen model ([`8b99881`](https://github.com/MedVisBonn/eyeseg/commit/8b99881ea91a9164515156447e726f9c7d4ff7e4))

* feat(eyeseg): commit latest changes ([`7c394e9`](https://github.com/MedVisBonn/eyeseg/commit/7c394e9c6bb02a45b841ad3a8271b9959d73f623))

* feat(Dockerfile): update to tensorflow 2.9.1 and set WORKDIR to /home/data by default ([`2709a68`](https://github.com/MedVisBonn/eyeseg/commit/2709a689e303cb5b86982fbd14d01b81921dddd8))

* feat(eyeseg): add train command to train model ([`1a86c2c`](https://github.com/MedVisBonn/eyeseg/commit/1a86c2c37cbdb6dd1a8129206ced6fd2246ae433))

* feat(scripts): separate drusen quantification from drusen computation; add plotting of overview and B-scans ([`3d8aa8e`](https://github.com/MedVisBonn/eyeseg/commit/3d8aa8ef1b31812aedf409a5cca18658beac36c7))

* feat(scripts): predict layers, compute drusen and quantify drusen with user defined grid ([`bec8d82`](https://github.com/MedVisBonn/eyeseg/commit/bec8d8245453acb137ece8e8d830fbd0b34a4191))

### Fix

* fix(pyproject.toml): update eyepie to 0.6.3 ([`1e065a2`](https://github.com/MedVisBonn/eyeseg/commit/1e065a23bdf0d4aae5666c0b485cead1a4ceed29))

* fix(quantify.py): add number of B-scans and correct volume name in results ([`d399227`](https://github.com/MedVisBonn/eyeseg/commit/d3992278fa20499eadf1b4bdff4ee29d8654445f))

* fix(plot-bscans): specify any folder in the input folder hierarchy to plot bscans for all contained volumes ([`3cf6ac1`](https://github.com/MedVisBonn/eyeseg/commit/3cf6ac1ceeb907d400a91208562ea47c781caae0))

* fix(scripts): keep folder structure of input for processed folder ([`bb6bcef`](https://github.com/MedVisBonn/eyeseg/commit/bb6bceff501638e5ab5251a4476f4b33f2104ac0))

* fix(plot_bscans.py): use all volumes if none are specified ([`c76b306`](https://github.com/MedVisBonn/eyeseg/commit/c76b306656d48c50cb6546ff98e1404cddea59d3))

* fix(scripts): fixed output_path overwrite and improve logging ([`d919cc1`](https://github.com/MedVisBonn/eyeseg/commit/d919cc1dee377998752168d30c89e9752a4a988d))

* fix(scripts): fix missing context for drusen command and missing output folder ([`e82e4b9`](https://github.com/MedVisBonn/eyeseg/commit/e82e4b95339d19fb7fc669564cd322c1f22ec13b))

### Refactor

* refactor(docker/Makefile): Clean unused variables and comment out image export ([`d01bb07`](https://github.com/MedVisBonn/eyeseg/commit/d01bb07911cfb8af9063031369d02f3a854f9dea))

* refactor(scripts): make minor improvements to the drusen and layers commands ([`9f344b5`](https://github.com/MedVisBonn/eyeseg/commit/9f344b5f83607711f673daeb19515c039125801b))

* refactor(scripts): prepared chaining of layers and drusen command ([`ce79f1b`](https://github.com/MedVisBonn/eyeseg/commit/ce79f1bad875ab9e2c9ed35bd519d554c4d6f7fb))

### Unknown

* Merge branch &#39;main&#39; of github.com:Oli4/eyeseg into main ([`61d2913`](https://github.com/MedVisBonn/eyeseg/commit/61d2913b4b0a5797096a1c624762dd63164d1340))

* Initial commit ([`9313728`](https://github.com/MedVisBonn/eyeseg/commit/93137284af9683962d1e25e76b74c3dba1241461))
