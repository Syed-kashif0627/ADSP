#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/types.h>
#include <string.h>

void listFiles(const char *path) {
    struct dirent *entry;
    DIR *dir = opendir(path);

    if (dir == NULL) {
        perror("Error opening directory");
        return;
    }

    while ((entry = readdir(dir)) != NULL) {
        // Skip the current and parent directory entries
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;

        // Print the file or directory name
        printf("%s/%s\n", path, entry->d_name);

        // If the entry is a directory, recursively traverse it
        if (entry->d_type == DT_DIR) {
            char newPath[1024];
            snprintf(newPath, sizeof(newPath), "%s/%s", path, entry->d_name);
            listFiles(newPath);
        }
    }

    closedir(dir);
}

int main(int argc, char *argv[]) {
    const char *path = (argc > 1) ? argv[1] : "."; // Default to current directory if no path is provided
    printf("Files in directory '%s':\n", path);
    listFiles(path);
    return 0;
}
