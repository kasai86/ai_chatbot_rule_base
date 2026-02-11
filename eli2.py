# -*- coding: utf-8 -*-

import eliza
import treetaggerwrapper

# ELIZA 初期化
t = eliza.eliza()

# TreeTagger 初期化
tagger = treetaggerwrapper.TreeTagger(
    TAGLANG='en',
    TAGDIR=r'D:\TreeTagger'
)

quit_word = 'q'

print "ELIZA mode: normal input"
print "TreeTagger mode: start input with ?"
print "Quit: q"

while True:
    user_input = raw_input("> ")

    # 終了判定
    if user_input == quit_word:
        print "Bye"
        break

    # 先頭が ? の場合 → TreeTagger
    if user_input.startswith('?'):
        text = user_input[1:]  # ? を削除

        if text.strip() == "":
            print "(no input for tagging)"
            continue

        tags = tagger.TagText(text)
        for tag in tags:
            print tag

    # それ以外 → ELIZA
    else:
        reply = t.respond(user_input)
        print reply
        
        