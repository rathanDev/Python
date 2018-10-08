from nltk.tree import ParentedTree


def traverse(tree, sentence):

    try:
        tree.label()

    except AttributeError:
        print ('--Err', sentence, tree)

    print ('tree', sentence, tree.height())

    if tree.height() <= 3:
        leaves = tree.leaves()
        print ('leaves', leaves)

        for leaf in leaves:
            print ('sentence1', sentence)
            sentence = sentence.replace(leaf, leaf.title())
            print ('sentence1', sentence)

        print ('sentence2', sentence)
        return sentence

    else:
        for child in tree:
            print ('child', sentence, child)

            if type(child) == str:
                print ('str child', child)
                continue

            else:
                return traverse(child, sentence)

        return sentence

def main():

    tree = ParentedTree.fromstring('(S '
                                   '    (NP alice) '
                                   '    (VP '
                                   '        (V chased) '
                                   '        (NP '
                                   '            (Det the) '
                                   '            (N rabbit)'
                                   '        )'
                                   '    )'
                                   ')')

    sentence = 'alice chased the rabbit'

    res = traverse(tree, sentence)

    print('res => ', res)


main()
