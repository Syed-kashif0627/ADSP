#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

int main(int argc, char *argv[]) {
    DIR *dir;
    struct dirent *entry;

    // Open the directory
    const char *path = (argc > 1) ? argv[1] : ".";
    dir = opendir(path);
    if (dir == NULL) {
        perror("Error opening directory");
        exit(EXIT_FAILURE);
    }

    printf("Contents of directory '%s':\n", path);

    // Read and print directory entries
    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;
        printf("%s\n", entry->d_name);
    }
    

    // Close the directory
    closedir(dir);

    return 0;
}
