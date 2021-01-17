Usage: main.py [OPTIONS]

Options:
  -c, --create          Create new rainbow table and write it to file
  -r, --read TEXT       path to existing rainbow table. FORMAT=hash:pass
  -t, --hash_type TEXT  Type of hash (md5, sha1, sha256)  [required]
  -w, --wordlist TEXT   link to wordlist i.e raw.github...
  -f, --filename TEXT   path to wordlist
  -o, --output TEXT
  -u, --url TEXT        url to scrape words from
  -h, --hash_str TEXT   Hash to find in rainbow table (only works in read
                        mode)

  --options TEXT        path to list of substrings to add to the wordlist
                        strings

  --help                Show this message and exit.

