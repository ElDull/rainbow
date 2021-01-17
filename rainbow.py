import click
import importlib
hashfuncs = importlib.import_module("hashfuncs")

@click.command()
@click.option('-c','--create', is_flag=True, help="Create new rainbow table and write it to file")
@click.option('-r','--read', help="path to existing rainbow table. FORMAT=hash:pass")

@click.option('-t', '--hash_type', required=True, help=f"Type of hash (md5, sha1, sha256)")
@click.option('-w', '--wordlist', help="link to wordlist i.e raw.github...")
@click.option('-f', '--filename', help="path to wordlist")
@click.option('-o', '--output', default="rainbow.txt", help='')
@click.option('-u', '--url', help="url to scrape words from")
@click.option('-h', '--hash_str', help="Hash to find in rainbow table (only works in read mode)")
@click.option('--options' ,help="path to list of substrings to add to the wordlist strings")

def main(create, read,hash_type,wordlist,filename,output, url, hash_str, options):
    d = {}
    opt = [""]

    if (create):
        try:
            with open(options, "r") as f:
                opt = [i.strip('\n') for i in f.readlines()]
                opt.append("")
        except:
            raise Exception("Bad Path to options file, use --help for more information")

        finally:
            pass

        if wordlist == None and filename == None and url == None:
            raise Exception("Please supply a path to a wordlist, use --help for more information")

        elif wordlist != None: 
            d = hashfuncs.populate_table_from_link(wordlist, hash_type,opt)

        elif filename != None:
            d = hashfuncs.populate_table_from_file(filename, hash_type, opt)

        elif url != None:
            d = hashfuncs.scrape_and_populate(url, hash_type, opt)

        with open(output, 'w') as f:
            for k,v in d.items():
                f.write(f"{k}:{v}\n")

    if(read is not None):
        try:
            with open(read, 'r') as f:
                for line in f.readlines():
                    hsh,passw = [i.replace("\n", "") for i in line.split(':')]
                    if hsh == hashfuncs.hash_string(hash_type, hash_str):
                        print(f'{hsh}:{passw}')
        except:
            raise Exception("Please supply a correct path to a wordlist, and a correct hash.\ntype see --help for more information")

                    

if __name__ == '__main__':
    main()
