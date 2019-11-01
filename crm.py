# This file is called primarily to run the app. It also defines the shell context for ease-of-use

from app import app, db
from app.models import User, Customer


# NOTE: With make_shell_context defined, we can run 'flask shell' from the command line and these elements will be pre-imported so 
# we don't have to go through the trouble manually.

@app.shell_context_processor                            # Allows us to pass this function to the app.shell_context_processor function
def make_shell_context():                               # This function will set the default environment
    return {'db':db, 'User':User, 'Customer':Customer}  # By default, we're going to import these
                                                       

if __name__ == '__main__':
    app.run(debug=True)