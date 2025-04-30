#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <pwd.h>
#include <grp.h>
#include <time.h>

void displayFileInfo(const char *path, const struct dirent *entry) {
    struct stat fileStat;
    char fullPath[1024];

    // Construct the full path to the file
    snprintf(fullPath, sizeof(fullPath), "%s/%s", path, entry->d_name);

    // Get file statistics
    if (stat(fullPath, &fileStat) == -1) {
        perror("Error retrieving file information");
        return;
    }

    // File permissions
    printf((S_ISDIR(fileStat.st_mode)) ? "d" : "-");
    printf((fileStat.st_mode & S_IRUSR) ? "r" : "-");
    printf((fileStat.st_mode & S_IWUSR) ? "w" : "-");
    printf((fileStat.st_mode & S_IXUSR) ? "x" : "-");
    printf((fileStat.st_mode & S_IRGRP) ? "r" : "-");
    printf((fileStat.st_mode & S_IWGRP) ? "w" : "-");
    printf((fileStat.st_mode & S_IXGRP) ? "x" : "-");
    printf((fileStat.st_mode & S_IROTH) ? "r" : "-");
    printf((fileStat.st_mode & S_IWOTH) ? "w" : "-");
    printf((fileStat.st_mode & S_IXOTH) ? "x" : "-");

    // Number of links
    printf(" %ld", fileStat.st_nlink);

    // Owner and group
    struct passwd *user = getpwuid(fileStat.st_uid);
    struct group *grp = getgrgid(fileStat.st_gid);
    printf(" %s %s", user ? user->pw_name : "unknown", grp ? grp->gr_name : "unknown");

    // File size
    printf(" %ld", fileStat.st_size);

    // Last modification time
    char timeBuf[80];
    strftime(timeBuf, sizeof(timeBuf), "%b %d %H:%M", localtime(&fileStat.st_mtime));
    printf(" %s", timeBuf);

    // File name
    printf(" %s\n", entry->d_name);
}

void listFiles(const char *path) {
    DIR *dir = opendir(path);
    struct dirent *entry;

    if (dir == NULL) {
        perror("Error opening directory");
        return;
    }

    while ((entry = readdir(dir)) != NULL) {
        // Skip "." and ".."
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;

        displayFileInfo(path, entry);
    }

    closedir(dir);
}

int main(int argc, char *argv[]) {
    const char *path = (argc > 1) ? argv[1] : ".";
    listFiles(path);
    return 0;
}
