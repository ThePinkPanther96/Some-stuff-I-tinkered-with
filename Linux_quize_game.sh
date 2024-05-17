#!/bin/bash

# create questions
function question() {
    question="$1"
    right_answer="$2"
    option_a="$3"
    option_b="$4"
    option_c="$5"

    while true; do
        echo "$question"
        echo "------------------------------------------------"
        echo "[A] $option_a"
        echo "[B] $option_b"
        echo "[C] $option_c"
        echo "------------------------------------------------"
        read -p "Enter your answer (or type 'q' to exit): " REPLY
        REPLY=$(echo "$REPLY" | tr '[:upper:]' '[:lower:]') 
        if [[ "$REPLY" = "q" ]]; then
            return 2
        elif [[ "$REPLY" = "a" || "$REPLY" = "b" || "$REPLY" = "c" ]]; then
            RIGHT_ANSWER=$(echo "$right_answer" | tr '[:upper:]' '[:lower:]')
            if [[ "$REPLY" = "$RIGHT_ANSWER" ]]; then
                echo "You are correct! $right_answer is the correct answer!"
                sleep 1
                return 0
            else
                echo "$REPLY is wrong Answer! The correct answer is $right_answer"
                sleep 1
                return 1
            fi
        else
            echo "Wrong input. Please enter one of the valid characters (A,B,C,a,b,c) or type 'quit' to exit." 
            echo ""
            sleep 1
        fi
    done
}

# Define an array to store questions and their arguments
questions=(
    "How was the inventor of Linux?" "A" "Linus Torvalds" "Xi Jinping" "Steve Wozniak"
    "On which distro is Ubuntu based on" "B" "RedHat" "Debian" "I use Arch BTW"
    "Which command is used to terminate process?" "C" "end" "rm" "kill"
    "Which is the best editor?" "A" "Vim" "Nano" "Word"
    "What kind of Linux ditsro do nubs and trolls use?" "B" "CentOS" "Arch" "Kali"
    "What is the name of the first Linux distro, created by Patrick Volkerding in 1993?" "C" "Fedora" "Debain" "Slackware"
    "Which of the following is not a Linux distribution?" "A" "Windows 10" "ZorinOS" "Gaia"
    "What is the name of the penguin mascot of Linux?" "B" "Pingu" "Tux" "Olaf"
    "What is the main programming language used in the development of the Linux kernel?" "C" "C++" "C#" "C"
    "Which Linux distro is known for its rolling release model and pacman package manager?" "A" "Arch" "Mint" "openSUSE"
    "What does the acronym GNU stand for in GNU/Linux?" "B" "Generalized Unix" "GNU's Not Unix" "Global Network Utility"
    "What is the name of the package manager used in Ubuntu?" "C" "yum" "pacman" "apt"
    "Who said: 'Linux is only free if your time has no value'?" "A" "Jamie Zawinski" "Cookie monster" "Steve Ballmer"
    "What is the name of the desktop environment commonly used in Linux distros?" "B" "KDE" "GNOME" "XFCE"
    "most servers in the world operates on?" "C" "Windows Core" "Just a kernel" "Linux"
    "Which Linux distro means 'humanity towards others' in South African philosophy?" "A" "Ubuntu" "Manjaro" "Mageia"
    "Which Linux command is known for its \"moo\" Easter egg?" "B" "cat" "cowsay" "ls"
    "Which were the best Rock band ever?" "C" "Arctic Monkeys" "AC\DC" "Pink Floyd"
    "What you should never do with Liux?" "A" "Install NVIDIA drivers" "Switch to Arch" "Unplugg from the wall"
    "Where are configuration files stored in Linux?" "B" "/bin" "/etc" "/usr"
    "Which is the most common used browser in Linux?" "C" "Tor browser" "Google Chrome" "Fire Fox"
    "In what year was linux invented on?" "A" "1991" "1983" "1969"
    "linux is based on what?" "B" "UNIX" " Linux kernel" "Basic"
    "What is the purpose of the \"strace\" command in Linux?" "C" "Monitor Packets" "Debugging" "to monitor interactions between processes"
    "Which Distro is commonly used for Cyber work?" "A" "Kali" "BlackArch" "Parrot OS"
)

# Define an array to store results
results=()

# Define a variable to track the total questions answered
total_questions=0

# Loop through questions
for (( i=0; i<${#questions[@]}; i+=5 )); do
    question "${questions[i]}" "${questions[i+1]}" "${questions[i+2]}" "${questions[i+3]}" "${questions[i+4]}"
    result=$?
    if [[ $result -eq 2 ]]; then
        break
    fi
    results+=("$result")
    total_questions=$((total_questions + 1))
done

# Calculate the score
correct_answers=$(grep -o '0' <<< "${results[@]}" | wc -l)
score=$((correct_answers * 100 / total_questions))

echo "Your score is: $score"
