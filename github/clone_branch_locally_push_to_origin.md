### 1. Clone branch
```
git clone -b TCGA_QUORRY_CRSV1902 git@sc.unc.edu:dbortone/dataset_prep.git TCGA_QUORRY_CRSV1902_dev_sae
```

### 2. change into new cloned branch
```
cd TCGA_QUORRY_CRSV1902_dev_sae/
```

### 3. Checkout new cloned branch
```
git checkout -b TCGA_QUORRY_CRSV1902_dev_sae
```

### 4. Make some changes to test & add
```
git add .
```

### 5. Check status
```
git status
```

### 6. Commit message
```
git commit -m "test creating branch from other branch locally, test changes to README"
```

### 7. Add new branch to repository
```
git push -u origin TCGA_QUORRY_CRSV1902_dev_sae
```
