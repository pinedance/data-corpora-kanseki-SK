# corpora-kanseki-SK

[ksnseki_repository](http://www.kanripo.org/)에 있는 사고전서 데이터

* [漢リポ Kanseki Repository](http://www.kanripo.org/)
* [漢リポ Kanseki Repository Github repo](https://github.com/kanripo)

## Usage

create `Kanseki_Repository.gitmodules` file

```bash
poetry run python build_gitmodules.py
```

clone submodules

```bash
bash git_clone_Kanseki_Repository.sh
```

merge texts of submodules

```bash
bash merge_and_split_text_files.sh
```

clean texts 

```bash
poetry run python clean_text.py
```


## Submodules

### Check

```bash
git submodule status
```

### Update

```bash
git submodule update --remote
```

### Remove

REF: [How do I revert my changes to a git submodule?](https://stackoverflow.com/a/27415757)

```bash
git submodule
git submodule deinit <path_to_submodule>
git rm <path_to_submodule>
rm -rf .git/modules/<path_to_submodule>
git commit -m "Removed submodule <path_to_submodule>"
```

remove all

```bash
git submodule
git submodule foreach git submodule deinit --all
git submodule foreach git rm -rf .
rm -rf .git/modules
git rm -rf 사고전서
git commit -m "Removed all submodules"
```

### Reset

REF: [How do I revert my changes to a git submodule?](https://stackoverflow.com/a/27415757)

```bash
git submodule
git submodule deinit -f .
git submodule update --init
```

REF: https://unstop.com/blog/git-submodule

## Download Data from git repo

```bash
NUM_FILES=10
INPUT_URL_BASE="https://github.com/pinedance/data-corpora-kanseki-SK/raw/main/DIST/clean"
OUTPUT_PATH="."

for ((i=1; i<=NUM_FILES; i++)); do
    INPUT_URL=$(printf "%s/%03d.txt" "$INPUT_URL_BASE" "$i")
    OUTPUT_FILE=$(printf "%s/%03d.txt" "$OUTPUT_PATH" "$i")
    curl -L -o "$OUTPUT_FILE" "$INPUT_URL"
```

