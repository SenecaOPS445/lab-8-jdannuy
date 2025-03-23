from fabric import Connection, task

@task
def setup(c):
    # Create a connection to the remote host
    conn = Connection(host='10.0.2.15', user='jdannuy', connect_kwargs={"password": "your_password"})

    # Update the remote server and install necessary packages
    print("Updating package list on remote server...")
    conn.sudo("apt update", password="your_password")

    # Install Apache2
    print("Installing Apache2...")
    conn.sudo("apt install -y apache2", password="your_password")

    print("Remote server setup completed!")
