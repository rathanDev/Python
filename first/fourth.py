from nltk.tree import ParentedTree


def traverse(tree, sentence):

    print ('tree', tree.height(), tree.label())

    if tree.label() == 'NP':

        for child in tree:

            try:
                print ('child', child)
                child.label()

            except AttributeError:
                print ('err', child)

            else:
                leaves = tree.leaves()
                print('leaves', leaves)
                for leaf in leaves:
                    sentence = sentence.replace(leaf, leaf.title())

                print ('sent', sentence)
                return sentence

    for child in tree:

        if type(child) == str:
            print ('str child', child)
            continue

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
#     expected output is 'alice chased The Rabbit'


main()
