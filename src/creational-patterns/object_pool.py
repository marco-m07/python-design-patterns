"""
Goal:
    Initializes a set of objects (pool) kept ready to use rather than allocating and 
    destroying them on demand.
Use cases:
    - When it is necessary to work with numerous objects that are particularly expensive 
    to instantiate and each object is only needed for a short period of time.
"""


class Connection:

    """
    Connection object (expensive to create).
    """

    def __init__(self) -> None:
        self._is_open = False

    @property
    def is_open(self) -> bool:
        return self._is_open
    
    @is_open.setter
    def is_open(self, value: bool) -> None:
        self._is_open = value

    def connect(self) -> None:
        print("Connecting...")
        self.is_open = True
    
    def reset(self) -> None:
        self.is_open = False

class ConnectionPool:

    """
    Connection pool that manages creation and
    vending of Connection objects.
    """

    _instance = None
    _connections = list()

    def __init__(self):
        if ConnectionPool._instance != None:
            raise NotImplemented("This is a singleton class.")

    @staticmethod
    def get_pool():
        if ConnectionPool._instance == None:
            ConnectionPool._instance = ConnectionPool()
        return ConnectionPool._instance
    
    def get_connection(self) -> Connection:
        if len(self._connections) >= 1:
            print("Returning existing connection.")
            return self._connections.pop(0)
        else:
            print("Creating new connection.")
            return Connection()
        
    def put_connection(self, conn: Connection) -> None:
        conn.reset()
        self._connections.append(conn)

def main():
    pool = ConnectionPool.get_pool()
    conn1 = pool.get_connection()
    conn2 = pool.get_connection()
    print("Connection1 status: {}".format(str(conn1.is_open)))
    conn1.connect()
    print("Connection1 status: {}".format(str(conn1.is_open)))
    pool.put_connection(conn1)
    pool.put_connection(conn2)
    conn3 = pool.get_connection()
    print("Is Connection3 the same object as Connection1? {}".format(conn1 is conn3))
    print("Is Connection3 the same object as Connection2? {}".format(conn1 is conn2))

if __name__ == "__main__":
    main()