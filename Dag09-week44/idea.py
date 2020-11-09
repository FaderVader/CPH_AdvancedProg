from collections import OrderedDict, defaultdict

def action_1(tb):
    tb.activate(Input.POWER)
    tb.is_active(Output(1))
    tb.is_active(Output(2))
    tb.is_active(Output(19))
    tb.is_active(Output(20))

def action_2(tb):
    tb.activate(Input(2)) # Input(2) = Input.IN_2
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.wait_for_input()
    #tb.wait_for_input()


# Option 1) Add them manually


actions = OrderedDict()

actions["action_1"] = action_1
actions["action_2"] = action_2

print(actions)

# Option 2) Create a decorator

# Define the decorator
def action(fn):
    actions[fn.__name__] = fn
    return fn

# Use the decorator
@action
def action_3(tb):
    tb.pulse(Input(7),1)
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    #tb.wait_for_input()

print(actions)

# Option 3) Scrape the dir()

# Reset actions
actions = OrderedDict()
for n, fn in list(globals().items()):
    if n.startswith("action_"):
        actions[n] = fn
print(actions)


# HOWTO: Call them one by one
tb = None # the current test runner
for n, fn in actions.items():
    print("Running " + n)
    print(fn(tb))


# Option 2b) Decorator with category

## Create a default dict which is instanciated with an empty list.
categories = defaultdict(list)

# Define the decorator
def action(category): 
    def decorator(fn):
        categories[category].append(fn.__name__)
        actions[fn.__name__] = fn
        return fn
    return decorator

# Use the decorator with category
@action("test af catering")
def action_3(tb):
    tb.pulse(Input(7),1)
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    #tb.wait_for_input()

print(categories["test af catering"])


