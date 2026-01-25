import shutil
import os


def copy_dir(src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)

    def recursive_copy(src_dir, dst_dir):
        contents = os.listdir(src_dir)
        if contents == []:
            return
        for item in contents:
            if os.path.isfile(os.path.join(src_dir, item)):
                shutil.copy(os.path.join(src_dir, item), os.path.join(dst_dir, item))
            else:
                new_src = os.path.join(src_dir, item)
                new_dir = os.path.join(dst_dir, item)
                os.mkdir(new_dir)
                recursive_copy(new_src, new_dir)
    recursive_copy(src_dir, dst_dir)


def main():
    copy_dir("/home/grayscaledev/Developer/github.com/static-site-generator/static/", "/home/grayscaledev/Developer/github.com/static-site-generator/public/")
main()
