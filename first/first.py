from nltk.tree import ParentedTree

# POS example

# Alice chased the rabbit
#(S (NP Alice) (VP (V chased) (NP (Det the) (N rabbit))))

# Congressional representatives are motivated by shiny money .
# (ROOT (S (NP (JJ Congressional) (NNS representatives)) (VP (VBP are) (VP (VBN motivated) (PP (IN by) (NP (NP (ADJ shiny) (NNS money))))))) (. .))


# Tree traversal to extrace words that need to be capitalized
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
            return sentence_

        for child in tree_:
            print('------- recursive call -------------')
            traverse_my_edit(child, sentence_)

def main():

    tree = ParentedTree.fromstring('(ROOT (S (NP (JJ Congressional) (NNS representatives)) (VP (VBP are) (VP (VBN motivated) (PP (IN by) (NP (NP (ADJ shiny) (NNS money))))))) (. .))')

    sentence = 'Congressional representatives are motivated by shiny money.'

    res = traverse_my_edit(tree, sentence)

    print('res => ', res)


main()
