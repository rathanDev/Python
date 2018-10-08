from nltk.tree import ParentedTree


def traverse_my_edit(tree_, sentence_):
    try:
        tree_.label()
    except AttributeError:
        print("-------------------exiting method --------------------")
        return

    else:
        if tree_.height() == 3 and tree_.label() == 'NP':   #child nodes
            for child in tree_:
                if child.height() == 2 and (child.label() == 'NN' or child.label() == 'NNP'):
                    leaves = tree_.leaves()
                    print(leaves)
                    for leaf in leaves:
                        temp_capital = leaf.capitalize()
                        sentence_ = sentence_.replace(leaf,temp_capital)
                        print(sentence_)
                else:
                    print('else2 ', child.height(), child.label())
            print('eof ', sentence_)
            return sentence_

        else:
            print('else1', tree_.height(), tree_.label())

        for child in tree_:
            print('------- recursive call -------------')
            traverse_my_edit(child, sentence_)


tree = ParentedTree.fromstring('(ROOT (S (NP (PRP he))(VP (VBD was)(NP (NP (DT the) (NN baldwin)) (PP (IN in) (`` ``) (NP (NN backdraft)))) (, ,)\
(`` ``)(NP(`` ``)(NP (RB sliver))(, ,) (`` ``)(CC and) (`` ``) (NP (JJ fair) (NN game))(SBAR (S (VP(`` ``)( (( ) \
(PP (IN with) (NP (NN cindy) (NN crawford)))(ADVP ( )))))))))(. .)))')

sentence = 'he was the baldwin in " backdraft , " " sliver , " and " fair game " ( with cindy crawford ) .'

traverse_my_edit(tree, sentence)
