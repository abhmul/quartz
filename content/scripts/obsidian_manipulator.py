from typing import Iterable, Tuple

import frontmatter
from frontmatter import Post
import glob
import argparse
import copy
import os
import re

from tqdm import tqdm

Posts = Iterable[Tuple[str, frontmatter.Post]]

GITIGNORE_PATH = ".gitignore"
MD_GLOB = "*.md"


parser = argparse.ArgumentParser(description="Script for various obsidian.md management tasks")
mx_group = parser.add_mutually_exclusive_group()
mx_group.add_argument("-cg", "--create_gitignore", action="store_true", help="Create a gitignore file from md files tagged to be ignored")
mx_group.add_argument("-mt", "--move_tag", help="Move this tag to the frontmatter")
mx_group.add_argument("-at", "--add_tag", help="Add a tag to files matching some glob")
mx_group.add_argument("-l", "--list_matches", action="store_true", help="List the files that were globbed")

parser.add_argument("--md_glob", default=MD_GLOB, help="files to glob for when running script")
parser.add_argument("--regex_filter", help="A regex to further filter results")
parser.add_argument("--debug", action="store_true", help="run script in debug mode")

# File utils
def safe_open_dir(dirpath: str) -> str:
    if not os.path.isdir(dirpath):
        print(f"Directory {dirpath} does not exist, creating it")
        os.makedirs(dirpath)
    return dirpath

def safe_create_file(filepath: str) -> str:
    dirpath = os.path.dirname(filepath)
    if dirpath != '':
        dirpath = safe_open_dir(dirpath)
    return filepath

# Specific stuff
def glob_md_files(md_glob: str, re_pattern: str = None):
    print(f"Globbing for markdown files using glob {md_glob}")
    md_files = glob.glob(md_glob)
    print(f"Globbed {len(md_files)} files.")
    if re_pattern is not None:
        print(f"Filtering globbed files using regex {re_pattern}")
        regex = re.compile(re_pattern)
        md_files = [f for f in md_files if (regex.match(f) is not None)]
        print(f"Kept {len(md_files)} files.")
    return md_files
    

def retrieve_frontmatter(files):
    print(f"Loading frontmatters from {len(files)} md files")
    return [(f, frontmatter.load(f)) for f in tqdm(files)]

def filter_gitignore(frontmatters):
    return [(f, fmatter) for f, fmatter in frontmatters if ("gitignore" in fmatter.get("tags", []))]

def fix_filepath(fpath):
    return fpath.replace(' ', '\\ ')

def write_gitignore(frontmatters, ignore_path=GITIGNORE_PATH):
    print(f"Writing {len(frontmatters)} files to gitignore.")
    with open(ignore_path, "w") as ignore_f:
        ignore_f.writelines(
            ["# Autogenerated file\n"] + \
                [f"{fix_filepath(f)}\n" for f, _ in frontmatters]
        )
    return True

def copy_post(post: Post):
    return Post(post.content, handler=post.handler, **copy.deepcopy(post.metadata))

def move_tag(posts: Posts, tag_name: str):
    modified_posts = []
    tag = f"#{tag_name}"
    for f, post in posts:
        if tag in post.content:
            new_post = copy_post(post)
            new_post.content = new_post.content.replace(tag, "")
            old_tags = list(new_post.get("tags", []))
            old_tags.append(tag_name)
            new_post["tags"] = list(set(old_tags))
            
            modified_posts.append((f, new_post))
    
    print(f"Moved tag {tag_name} to frontmatter in {len(modified_posts)} md files.")
    return modified_posts

def add_tag(post: Posts, tag_name: str):
    modified_posts = []
    for f, post in posts:
        new_post = copy_post(post)
        old_tags = list(new_post.get("tags", []))
        old_tags.append(tag_name)
        new_post["tags"] = list(set(old_tags))
        
        modified_posts.append((f, new_post))
    
    print(f"Added tag {tag_name} to frontmatter in {len(modified_posts)} md files.")
    return modified_posts

def debug_path(fpath: str, debug=False):
    return f"tmp/{fpath}" if debug else fpath

def write_posts(posts: Posts, debug=False):
    print(f"Writing {len(posts)} markdown files")
    for f, post in tqdm(posts):
        write_name = debug_path(fpath=f, debug=debug)
        with open(safe_create_file(write_name), "wb") as write_file:
            frontmatter.dump(post, write_file)

    
if __name__ == "__main__":
    args = parser.parse_args()
    
    markdown_files = glob_md_files(args.md_glob, re_pattern=args.regex_filter)
    posts = retrieve_frontmatter(markdown_files)
    
    if args.create_gitignore:
        print("Creating a gitignore")
        posts = filter_gitignore(posts)
        write_gitignore(posts, ignore_path=debug_path(GITIGNORE_PATH, debug=args.debug))
    
    elif args.move_tag is not None:
        print(f"Moving tag {args.move_tag} to frontmatter")
        modified_posts = move_tag(posts, tag_name=args.move_tag)
        write_posts(modified_posts, debug=args.debug)
    
    elif args.add_tag is not None:
        print(f"Running add_tag command for tag {args.add_tag}")
        modified_posts = add_tag(posts, tag_name=args.add_tag)
        write_posts(modified_posts, debug=args.debug)
    
    elif args.list_matches:
        print("Listing matches")
        print("=======================")
        print("\n".join(markdown_files))
        
    
        
    
    
