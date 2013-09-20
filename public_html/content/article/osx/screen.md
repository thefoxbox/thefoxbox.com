GNU Screen in Mac OSX
=====================

Dynamic Terminal titles
-----------------------

### ~/.bashrc

    :::bash
    case ${TERM} in
        xterm*)
            PROMPT_COMMAND='printf "\033]0;%s@%s:%s\007" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/~}"'
            ;;
        screen*)
            PROMPT_COMMAND='printf "\033]0;%s@%s:%s\033\\" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/~}"'
            ;;
    esac

    [ "$PS1" = "\\s-\\v\\\$ " ] && PS1="[\u@\h \W]\\$ "

### ~/.bash_profile

    :::bash
    if [ -f ~/.bashrc ]; then
        . ~/.bashrc
    fi

    PS1='[\u@\h \W]\\$ '

### ~/.screenrc

    :::bash
    startup_message off
    defscrollback 5000
    altscreen on
    hardstatus off
    termcapinfo xterm* 'hs:ts=\E]2;:fs=\007:ds=\E]2;screen\007'
