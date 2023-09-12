from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname' : 'Support Inventory',
        'name': 'Michael Marcellino Satyanegara',
        'class': 'PBP E',
        
        'namefood': 'Seafoam Pudding',
        'amountfood': '5',
        'descriptionfood': (
            'Type            : Food\n'
            'Healing Value   : 160~200\n'
            'Status Effect   : Attack (<span class="green-text">+50%</span>)\n'
            '                  Speed (<span class="green-text">+10%</span>)\n'
            '                  Critical Chance (<span class="green-text">+10%</span>)\n'
            '                  Critical Damage (<span class="green-text">+25%</span>)\n'
            '                  Health Point (<span class="red-text">-25%</span>)\n'
            '                  Defend (<span class="red-text">-25%</span>)\n'
            'Cooldown Time   : 100 Seconds\n'
            'Rarity Class    : <span class="purple-text">Epic</span>'
        ),
        'pricefood' : (
            'Buy     : 100 Stardust\n'
            'Sell    : 75 Stardust'),
        
        'nameamulet': 'Magic Rock Candy',
        'amountamulet': '1',
        'descriptionamulet': (
            'Type            : Amulet\n'
            'Status Effect   : All Attribute (<span class="green-text">+50%</span>)\n'
            'Passive Skill   : Heals the user by 100 every 10 seconds\n'
            'Active Skill    : Creates a beam that blinds the opponent for 3 seconds\n'
            'Cooldown Skill  : 60 Seconds\n'
            'Rarity Class    : <span class="yellow-text">Legendary</span>'
        ),
        'priceamulet' : (
            'Buy     : -\n'
            'Sell    : <span class="red-text">There is only one of this item (0 Stardust)</span>')
    }

    return render(request, "main.html", context)