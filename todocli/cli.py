import sys, json, os
from pathlib import Path


from .__version__ import __version__

def version( ):
    print( f'todocli {__version__}' )


def get_todos_file( ):
    '''Get the path to the todos.json file in the user\'s home directory.'''
    return Path.home( ) / '.todocli.json'


def load_todos():
    """Load todos from the JSON file."""


    todos_file=get_todos_file()
    if not todos_file.exists( ):
        return[ ]
    
    try:
        with open(todos_file,'r')as f:
            return json.load( f )
    except( json.JSONDecodeError,IOError ):
        return [ ]


def save_todos( todos ):
    '''Save todos to the JSON file.'''
    todos_file=get_todos_file( )
    try:
        with open( todos_file,'w' ) as f:
            json.dump(todos,f,indent=2)
    except IOError as e:
        print(f'Error saving todos: {e}')
        sys.exit( 1 )


def add_todo(task):
    """Add a new todo item."""

    if not task.strip( ):
        print( "Error: Todo task cannot be empty" )
        sys.exit(1)
    


    todos=load_todos( )
    todo_item={
        'id':len( todos )+1,
        'task':task.strip(),
        'completed':False
    }
    todos.append(todo_item)
    save_todos( todos )
    print(f"Added todo: {task.strip( )}")


def list_todos( ):
    '''List all todo items.'''
    todos=load_todos()
    

    if not todos:
        print( 'No todos found. Add some with \'todocli add "Your task"\'' )
        return
    

    print( 'Your todos:' )
    for todo in todos:
        status='✓'if todo['completed']else'○'
        print(f'  {status} {todo["id"]}: {todo["task"]}')


def help():


    print( "Usage: todocli [OPTIONS] COMMAND [ARGS]..." )
    print( "Options:" )
    print( "  -v, --version  Show the version and exit." )
    print( "  -h, --help     Show this message and exit." )
    print( "Commands:" )
    print( "  help          Show this message and exit." )
    print( "  add TASK      Add a new todo item." )
    print( "  list          List all todo items." )


def cli():
    if len( sys.argv )>1:
        if sys.argv[ 1 ]in( '-v','--version' ):
            version( )
            return
        elif sys.argv[1]in('-h','help','--help'):
            help()
            return
        elif sys.argv[ 1 ]=='add':
            if len(sys.argv)<3:
                print( 'Error: Please provide a task to add' )
                print( 'Usage: todocli add "Your task"' )
                sys.exit( 1 )
            task=' '.join( sys.argv[ 2: ] )
            add_todo( task )
            return
        elif sys.argv[1]=='list':
            list_todos()
            return
        else:
            print(f'Unknown command: {sys.argv[1]}')
            print( 'Run \'todocli help\' for usage information.' )
            sys.exit(1)
    
    # Default behavior - show help when no command is given
    help()
