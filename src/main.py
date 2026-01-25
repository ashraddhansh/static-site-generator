from os.path import isfile, join
import shutil
import os
from generate_page import generate_page


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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)
    if items == []:
        return
    for item in items:
        if os.path.isfile(os.path.join(dir_path_content, item)):
            generate_page(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, f'{item.split(".")[0]}.html'))
        else:
            new_dir_path_content = os.path.join(dir_path_content, item)
            new_dest_dir_path = os.path.join(dest_dir_path, item)
            os.makedirs(new_dir_path_content, exist_ok = True)
            generate_pages_recursive(new_dir_path_content, template_path, new_dest_dir_path)




def main():
    copy_dir("/home/grayscaledev/Developer/github.com/static-site-generator/static/", "/home/grayscaledev/Developer/github.com/static-site-generator/public/")
    start_path = "/home/grayscaledev/Developer/github.com/static-site-generator"
    generate_pages_recursive(start_path + "/content/", start_path + "/template.html", start_path + "/public/")

main()
