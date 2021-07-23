#
# ~/.bashrc
#
# Welcome to Mia's /comfy/ bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#alias section
alias bye='shutdown -h now'
alias e='exit'
alias v='vim'
alias grep='grep --color=auto'
alias ls='ls --color=auto'
alias la='ls -a'
alias htop='htop -t'
alias r="ranger"

#PS1='[\u]'
PS1='[\u@\h \W]\$ '
shopt -s autocd


#Import colorschemefrom wal
(cat /home/$USER/.cache/wal/sequences)
