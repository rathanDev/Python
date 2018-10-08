from nltk.tree import ParentedTree

# POS example

# Alice chased the rabbit
#(S (NP Alice) (VP (V chased) (NP (Det the) (N rabbit))))

# Congressional representatives are motivated by shiny money .
# (ROOT (S (NP (JJ Congressional) (NNS representatives)) (VP (VBP are) (VP (VBN motivated) (PP (IN by) (NP (NP (ADJ shiny) (NNS money))))))) (. .))


# Tree traversal to extrace words that need to be capitalized
def traverse_my_edit(tree, sentence):

    try:
        tree.label()

    except AttributeError:
        print("----------Error")

        return

    else:

        print('I tree ', tree.height(), tree.label())
        if tree.height() == 3 and tree.label() == 'NP':   #child nodes

            sentence = sentence
            for child in tree:

                print('child', child.height(), child.label())
                if child.height() == 2 and (child.label() == 'N'):                            #and (child.label() == 'NN' or child.label() == 'NNP'):
                    leaves = tree.leaves()
                    print('leaves', leaves)
                    for leaf in leaves:
                        sentence = sentence.replace(leaf, leaf.title())

                    print('1', sentence)

            print('M tree ', tree.height(), tree.label())
            print('2', sentence)
            return sentence

        print('E tree ', tree.height(), tree.label())
        print(sentence)

        for child in tree:
            print('child', child)
            traverse_my_edit(child, sentence)


def main():

    tree = ParentedTree.fromstring('(S '
                                   '    (NP Alice) '
                                   '    (VP '
                                   '        (V chased) '
                                   '        (NP '
                                   '            (Det the) '
                                   '            (N rabbit)'
                                   '        )'
                                   '    )'
                                   ')')

    sentence = 'Alice chased the rabbit'

    res = traverse_my_edit(tree, sentence)

    print('res => ', res)


main()
