from nltk.tree import ParentedTree


# Tree traversal to extrace words that need to be capitalized
def traverse_my_edit(tree_, sentence_):

    try:
        tree_.label()

    except AttributeError:
        print("-------------------Error ")
        return

    else:

        print('tree_.label', tree_.label())

        if tree_.height() == 3 and tree_.label() == 'NP':   #child nodes
            for child in tree_:
                if child.height() == 2 and (child.label() == 'NN' or child.label() == 'NNP'):
                    leaves = tree_.leaves()
                    print('tree_.leaves', leaves)
                    for leaf in leaves:
                        temp_capital = leaf.capitalize()
                        sentence_ = sentence_.replace(leaf,temp_capital)
                        print('sentence', sentence_)

            return sentence_

        print('tree_.height', tree_.height())
        for child in tree_:
            traverse_my_edit(child, sentence_)


def main():

    tree = ParentedTree.fromstring('(ROOT (S (NP (PRP he))(VP (VBD was)(NP (NP (DT the) (NN baldwin)) (PP (IN in) (`` ``) (NP (NN backdraft)))) (, ,)\
    (`` ``)(NP(`` ``)(NP (RB sliver))(, ,) (`` ``)(CC and) (`` ``) (NP (JJ fair) (NN game))(SBAR (S (VP(`` ``)( (( ) \
    (PP (IN with) (NP (NN cindy) (NN crawford)))(ADVP ( )))))))))(. .)))')

    sentence = 'he was the baldwin in " backdraft , " " sliver , " and " fair game " ( with cindy crawford ) .'

    res = traverse_my_edit(tree, sentence)

    print('res => ', res)


main()
