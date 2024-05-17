#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail


logging () {
    function="$1"
    level="$2"
    message="$3"

    local current_date=$(date +"%d/%m/%Y-%H:%M:%S")
    local file_timestamp=$(date +"%A_%d_%m_%Y")
    local log_file_path="${LOG_DIR}${file_timestamp}.log"
    local log_entry="$current_date - [$level][$function] - $message"

    mkdir -p "$(dirname "$log_file_path")"
    echo "$log_entry" >> "$log_file_path"
}


EDUCATION_DIR="/home/education"
DEVELOPMENT_DIR="/home/development"
PERSONAL_DIR="/home/personal"

path_list=(
    "$PERSONAL_DIR"
    "$DEVELOPMENT_DIR"
    "$EDUCATION_DIR"
    "$EDUCATION_DIR/courses"
    "$EDUCATION_DIR/books"
    "$DEVELOPMENT_DIR/projects"
    "$DEVELOPMENT_DIR/archives"
    "$DEVELOPMENT_DIR/tools"
    "$PERSONAL_DIR/music"
    "$DEVELOPMENT_DIR/videos"
    "$DEVELOPMENT_DIR/pictures"
)

configure_tree () {
    for path in "${path_list[@]}"; do
        if [ ! -d "$path" ]; then
            sudo mkdir -p $path
        else
            echo "$path exists. Moving to the next path\n"
        fi
    done
}


add_object () {
    source_path="$1"
    target_path="$2"
    local added_object="${source_path##*/}"
    local object_extension="${added_object##*.}"
    local dev_extensions=("zip" "tar.gz" "sh" "py" "md")
    local education_extensions=("pdf" "docx" "txt")
    local personal_extensions=("mp3" "mp4" "jpg" "png")

    local section
    if [[ "$target_path" == *"/development"* ]]; then
        section="development"
        valid_extensions=("${dev_extensions[@]}")
    elif [[ "$target_path" == *"/education"* ]]; then
        section="education"
        valid_extensions=("${education_extensions[@]}")
    elif [[ "$target_path" == *"/personal"* ]]; then
        section="personal"
        valid_extensions=("${personal_extensions[@]}")
    else
        echo "Invalid target directory."
        return 1
    fi
    if [[ " ${valid_extensions[@]} " =~ " $object_extension " ]]; then
        mv "$source_path" "$target_path"
        echo "Item '$added_object' moved to '$target_path'."
    else
        echo "Extension '$object_extension' not allowed in the '$section' section."
        return 1
    fi
}

# edit according to console logging like in the backup file 
delete_object () {
    object_to_delete="$1"
    if [ -e "$object_to_delete" ]; then
        sudo rm -rf "$object_to_delete"
        if [ ! -e "$object_to_delete" ]; then
            echo "$object_to_delete was deleted successfully" 
        else
            echo "Failed to delete $object_to_delete" 
            return 1
        fi
    else
        echo "File $object_to_delete does not exist or cannot be accessed"
        return 1
    fi
}


modify_object () {
    current_name="$1"
    new_name="$2"
    if [ -e "${current_name}" ]; then
        sudo mv "$current_name" "$new_name"
        if [ -e "${new_name}" ]; then
            echo "${current_name} renamed to ${new_name}" 
        else
            echo "Failed to rename ${current_name} to ${new_name}" 
            return 1
        fi
    else
        echo "Failed to complete operation"
        return 1
    fi
}

are_you_sure () {
    read -p "Are you sure you want to continue with the operation? (Y/N): " replay
    if [ "${replay}" == "Y" ] || [ "${replay}" == "y" ]; then 
        return 0 
    fi
    if [ "${replay}" == "N" ] || [ "${replay}" == "n" ]; then
        exit 0 
    fi
}

main () {
    while true; do
        configure_tree
        echo "$(sed -n '1,8p' main_menu.txt)"
        read
        if [[ "${REPLY}" = "1" ]]; then
            while true; do
                read -p "Enter SOURCE path with file name: " source_path
                read -p "Enter TARGET path with file name: " target_path
                if [[ -z "$source_path" || -z "$target_path" ]]; then
                    echo "$(sed -n '12p' main_menu.txt)"
                else
                    are_you_sure
                    add_object "$source_path" "$target_path"
                    sleep 1
                    main
                fi
            done
        fi
        if [[ "${REPLY}" = "2" ]]; then
            while true; do
                read -p "Enter to delete with full path: " path
                if [[ -z "$path" ]]; then
                    echo "$(sed -n '14,15p' main_menu.txt)"
                else
                    are_you_sure
                    delete_object "$path"
                    sleep 1
                    main
                fi
            done
        fi
        if [[ "${REPLY}" = "3" ]]; then
            while true; do
                read -p "Enter name of item to modify including directory/sub-directory: " corrent_name
                read -p "Enter new name of  item to modify including directory/sub-directory: " new_name
                if [[ -z "$corrent_name" || -z "$new_name" ]]; then
                    echo "$(sed -n '17,18p' main_menu.txt)"
                else
                    are_you_sure
                    modify_object "$corrent_name" "$new_name"
                    sleep 1
                    main
                fi
            done
        fi
        if [[ "${REPLY}" = "4" ]]; then
            echo "Exiting..."
            sleep 1
            exit
        fi
    done
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main
fi