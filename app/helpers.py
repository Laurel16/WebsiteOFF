def cat_emoij(x, my_dict):
    if x.startswith("J'hésite"):
        return '🤔'

    for k, v in my_dict.items():
        if k in x:
            return v


list_categories = {'appetizers' : '🥨',
                     'artificially sweetened beverages': '🧃',
                     'biscuits and cakes': '🍰',
                     'bread': '🥖 🍞',
                     'breakfast cereals': '🥐',
                     'cereals':'🛌',
                     'cheese': '🧀',
                     'chocolate products': '🍫',
                     'dairy desserts': '🍮',
                     'dressings and sauces': '🥫',
                     'dried fruits': '🍑',
                     'eggs': '🥚',
                     'fats': '🧈',
                     'fish and seafood': '🐠',
                     'fruit juices': '🧃',
                     'fruit nectars': '🧃',
                     'fruits': '🍇',
                     'ice cream': '🍦',
                     'legumes': '🥦',
                     'meat': '🥩',
                     'milk and yogurt': '🥛',
                     'nuts': '🥥',
                     'offals': '🥩',
                     'one dish meals': '🍲',
                     'pastries': '🍩',
                     'pizza pies and quiche': '🍕',
                     'plant based milk substitutes': '🍶',
                     'potatoes': '🥔',
                     'processed meat': '🍖',
                     'salty and fatty products': '🍟',
                     'sandwiches': '🥪',
                     'soups': '🍜',
                     'sweetened beverages': '🥤',
                     'sweets': '🍭',
                     'teas and herbal teas and coffees': '☕️',
                     'unsweetened beverages': '🍵',
                     'vegetables': '🥬',
                     'waters and flavored waters':'💧'}
