HISTFILE=~/.histfile
HISTSIZE=10000
SAVEHIST=10000
setopt appendhistory autocd extendedglob nomatch notify
setopt auto_pushd
setopt prompt_subst
setopt share_history
unsetopt beep
bindkey -e
autoload -Uz compinit
compinit

export HOST=`hostname`
#teminal dependent settings
case "$TERM" in
    xterm*|rxvt*)
        precmd() {
            echo -ne "\033]0;${USER}@`hostname`: ${PWD/$HOME/~}\007"
        }
        #prompt
        local ESC=`echo '\e'`
        local GREEN="%{${ESC}[1;32m%}"
        local BLUE=$'%{\e[1;34m%}'
        local RED=$'%{\e[1;31m%}'
        local DEFAULT=$'%{\e[1;m%}'
        PROMPT=$BLUE'[${USER}@${HOST}] '$DEFAULT
        RPROMPT=$RED'`gxpc prompt 2> /dev/null`'$GREEN'[%~]'$DEFAULT
        ;;
    screen*)
        # title name
        precmd() {
            echo -ne "\ek$(basename $(pwd))\e\\"
            echo -ne "\033]0;${USER}@`hostname`: ${PWD/$HOME/~}\007"
        }
        preexec(){
            echo -ne "\ek#${1%% *}\e\\"
        }
        #prompt
        local ESC=`echo '\e'`
        local GREEN="%{${ESC}[1;32m%}"
        local BLUE=$'%{\e[1;34m%}'
        local RED=$'%{\e[1;31m%}'
        local DEFAULT=$'%{\e[1;m%}'
        PROMPT=$BLUE'[${USER}@${HOST}] '$DEFAULT
        RPROMPT=$RED'`gxpc prompt 2> /dev/null`'$GREEN'[%~]'$DEFAULT
        ;;
esac

alias ls='ls -F'
#alias pdsh="pdsh -R ssh -g .all"
#alias pdcp="pdcp -R ssh -g .all"

export EDITOR="vim"

#zsh style
#zsh 補完候補を ←↓↑→ でも選択出来るようにする
zstyle ':completion:*:default' menu select=2

# PyPy3でのテスト実施
alias test='oj t -c "pypy3 main.py" -d ./tests/'
# Pythonでのテスト実施
alias test2='oj t -c "python3 main.py" -d ./tests/'

# PyPy3での解答提出
alias sb='acc s main.py -- --guess-python-interpreter pypy'
# Pythonでの解答提出
alias sb2='acc s main.py'

# コンテストフォルダへ移動
alias c='cd contest'

# main.pyを開く
alias o='code main.py'

# 出力確認用
alias d='python main.py'
