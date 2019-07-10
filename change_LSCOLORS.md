
## How to install LSColors on a new Macbook

### 1. Install homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 2. Install coreutils
```
brew install coreutils
```

### 3. Create .dir_colors file
```
gdircolors -p > ~/.dir_colors
```

### 4. Add following lines to ~/.bashrc

```
eval `gdircolors ~/.dir_colors`
alias ls="gls --color=auto"
alias ll="gls --color=auto -lh"
alias la="gls --color=auto -a"
```

### 5. Add following line to ~./bash_profile
```
source ~/.bashrc
```

### 6. Run following command to make changes
```
source .bash_profile
```
