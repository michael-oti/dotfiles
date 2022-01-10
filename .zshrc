# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.config/oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="oxide"

plugins=(git zsh-z)

export EDITOR=/usr/bin/micro
export MICRO_TRUECOLOR=1

source $ZSH/oh-my-zsh.sh
source ./.config/nnn/config

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

alias nnn="nnn -e"
alias ls="exa -alh"


if [ -z "$TMUX" ]
then
    tmux attach -t TMUX || tmux new -s TMUX
fi

