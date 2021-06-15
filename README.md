# Python-Chatroom
I created Python Chatroom Based On TCP protocols. A Simple Chatroom To Help Do communication over socket and threading.
Python ChatRoom Based on TCP AI 
![image](https://user-images.githubusercontent.com/75814453/122125194-96a0ff00-ce49-11eb-81a8-d28bebc61b19.png)

Project Presentation [project.pptx](https://github.com/F4LL-Dev/Python-Chatroom/files/6658832/project.pptx)

<p dir="ltr">

</p>

<p dir="ltr">
    Title: AI TCP ChatRoom In Python
</p>
<h1 dir="ltr">
    Chapter 1 - Introductory
</h1>
<h2 dir="ltr">
    1.1 Introduction:
</h2>
<p dir="ltr">
    The chatroom is excellent for communication over the network and the TCP
    connection ensures reliability.TCP Chatroom is built via the computer
    networking programming language Python3 which is the latest one. This TCP
    chatroom enables us to have one server that hosts the chat while multiple
    clients are connected to it and then communicate with each other via the
    main server.
</p>
<br/>
<p dir="ltr">
    This is a full-working chatroom, and you can easily send and receive
    messages also over the internet and locally by using the server’s IP. The
    port needs to be opened for the public connection.
</p>
<br/>
<p dir="ltr">
    Another advantage of this chatroom is that a rule of kicking and banning is
    activated as the admin site which is implemented using AI techniques so
    that the errors can be handled in such a way that becomes useful and
    trigger specific operation.
</p>
<h2 dir="ltr">
    1.2 Abstract:
</h2>
<p dir="ltr">
    We’ve built a chatroom in python based on TCP protocols. The TCP protocol
    is the transmission control protocol so that the communication between
    clients to clients and clients to servers is reliable. The message
    transmitted over TCP sends the report back to the server if any error
    occurred why it is more preferable to UDP.
</p>
<br/>
<p dir="ltr">
    While using python3 we used multi-threading and socket language to
    implement it using two libraries socket and threading and whenever a client
    connects to the network a new thread is generated to handle it. So on
    disconnection of the client, an error-handling procedure is the cause of
    the helping source to tell the server that there is an error triggered at
    the client side which is ultimately taken as client disconnection.
</p>
<br/>
<p dir="ltr">
    We have established a server-client network, where the messages are
    centralized and each client talks to others via the centralized server. The
    non-reserved port is assigned to the server.
</p>
<h3 dir="ltr">
    1.2.1 Server-Client Network:
</h3>
<p dir="ltr">
    <img
        src="https://lh3.googleusercontent.com/f5hL2dx8CHZ0I0Axd2-zwvZmNvxwYdYNBEsHVA9wl0lpdMrVzbzpvfCX11VZteTj8TfHlqqPrG9pYKaQVOwdGJYQPxoLlz0xypJ91jOa8PahKb24rfGhqELtwtq71L3mD6mcXiv_"
        width="475"
        height="290"
    />
</p>
<ul>
    <li dir="ltr">
        <h4 dir="ltr">
            1.2.1.1 Server-side:
        </h4>
    </li>
</ul>
<p dir="ltr">
    On the server-side, the server is established using an INET socket and TCP
    connection. The IP is used as the server’s IP and the port is the
    non-reserved one. The server always receiving the client’s messages while
    multiple threads are running for multiple clients. It accepts the client
    connection.
</p>
<p dir="ltr">
    The message is broadcasted to all clients via the server.
</p>
<ul>
    <li dir="ltr">
        <h4 dir="ltr">
            1.2.1.2 Client-Side:
        </h4>
    </li>
</ul>
<p dir="ltr">
    On the client-side, the running server’s IP and port are needed to connect
    to it. After a successful connection, it then needs to write the message to
    broadcast via the server. There are two threads on the client-side, one for
    receiving and others for writing messages. Broadcasted messages are shown
    on each client.
</p>
<p dir="ltr">
    The server must be running for the Client. On the server side, 3 different
    modules manage, broadcast the messages, and receives the messages from the
    client.
</p>
<ul>
    <li dir="ltr">
        <h4 dir="ltr">
            1.2.1.3 Extra Powers and Features:
        </h4>
    </li>
</ul>
<p dir="ltr">
    Extra powers and features are the functionality of a user to kick and ban a
    specific user based on the implementation of kicking and banning algo.
    implemented by using the AI techniques to handle the clients in such a way
    that the error can be used to add the client to the ban list or kick. If
    the client has been kicked then he can rejoin. But if he was banned, he
    wasn’t able to come back and a bann option occurs until he gets unbanned.
</p>
<br/>
<h2 dir="ltr">
    1.3 Pros of Our TCP Chatroom:
</h2>
<ol>
    <li dir="ltr">
        <p dir="ltr">
            Based on Latest Python 3 which is more reliable which supports the
            latest technology.
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            The total software size is less than an MB so even a computer with
            less than a 500 MB ram can run it.
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            LAN compatible.
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            WAN compatible ( By specifying open ports and host address).
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            Multi-threading is compatible.
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            ASCII encryption for messages.
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            TCP is based on reliable communication.
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            Structural programming.
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            Upgradable.
        </p>
    </li>
</ol>
<h2 dir="ltr">
    1.4 Technology:
</h2>
<ul>
    <li dir="ltr">
        <p dir="ltr">
            Python 3
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            Pycharm
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            Windows 10
        </p>
    </li>
</ul>
<h2 dir="ltr">
    1.5 Requirements:
</h2>
<ul>
    <li dir="ltr">
        <p dir="ltr">
            Python 3
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            500MB Ram, 10MB storage
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            Multi-threading CPU ( Recommended)
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            Python enabled machine
        </p>
    </li>
</ul>
<h1 dir="ltr">
    Chapter 2 Methodology:
</h1>
<br/>
<p dir="ltr">
    The procedure for Implementing the server:
</p>
<ul>
    <li dir="ltr">
        <h2 dir="ltr">
            2.1 Server Implementation:
        </h2>
    </li>
</ul>
<ol>
    <li dir="ltr">
        <p dir="ltr">
            For Network connection and performing operations, we have imported
            two library files, socket, and threading.
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh6.googleusercontent.com/XCO1AHtoH9TXg_wvJO8JGwaU7ZOZvh8HYec2vkxc9_knI3RkUrNuCcpwtHvrNsQv84_VDS2gFduPdtCC76koFr93rIMFIH4RHAq2eSTtnLl3QfP2y5LwKC6z14mWA6xo5d4y_8Wh"
        width="426"
        height="46"
    />
</p>
<ol start="2">
    <li dir="ltr">
        <p dir="ltr">
            The host address is generated, in this, we use the localhost
            address but for the server. The server address has to be used and
            the port which is not reserved is to be used.
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh6.googleusercontent.com/kejZ9YG3SaMnteV7DQXGHYdnBcis2Z5xS-oTVtJ8iYVCSOjcGbUj5Vui1RrM5kt5_RXQFZw_1kIKWzr5QUOhY2M2-76fVB4sPrNzTeb2X60kWL9dKLJxIEcPhkOX1LxcuhdSe0Az"
        width="474"
        height="71"
    />
</p>
<ol start="3">
    <li dir="ltr">
        <p dir="ltr">
            The server socket is defined using AF_INET for internet socket and
            SOCK_STREAM for TCP protocols. Then the listen() module starts the
            server to listen.
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh4.googleusercontent.com/s3qSCzPG4AWQXeKZT0s0auwPdApDsUnUhvF5gvI-_0GrQe7XiITWjCBAoalibkOImH9r7Ijd8-pEEh6QwE-AxQSMkzFxpGThpfBZyo5eVb3bDUSNqj03zV-3HJTJHbL32LpezOg2"
        width="541"
        height="76"
    />
</p>
<ol start="4">
    <li dir="ltr">
        <p dir="ltr">
            Two lists are generated to store clients and their nicknames. Then
            the module Broadcast is used for broadcasting the messages to all
            clients are created.
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh5.googleusercontent.com/s3-CKox5YLkMR0zawY0j4sSpa1nUEWV-n8bQj72fhy1o-7bPoCE2u5La5dX7er5zP0khd5w30JusgalJGdrDinIP_L_3tQ-s7sRx11YKWCG8_uRHi50Cd9lw36kTLTpknimawJn5"
        width="560"
        height="70"
    />
</p>
<ol start="5">
    <li dir="ltr">
        <p dir="ltr">
            The module manage gets client as an argument is used for managing
            the client’s request and broadcast the messages to all clients. if
            an exception occurs the client is removed and a disconnection
            interrupt is broadcasted to the rest clients the loop is then
            terminated to close the thread.
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh4.googleusercontent.com/zI3kiFuOCzAio_fgu5XBo6TDKTkQa0xhsmSWukrSWm3j2AL4lni5LVhz3x3AGXqBBuzz_QrGbGShxgF1D-0hEznDXCNNqJAXerP51JdRA7tnYTvE6vPQS_Kny34Qb71Z61MCv_Y5"
        width="548"
        height="385"
    />
</p>
<p dir="ltr">
    If the message is kick or ban from the user then if the user is admin then
    specific command is executed. and on the execution of the ban command
    banned nickname is added to the bans.txt.
</p>
<p dir="ltr">
    Exception Handling:
</p>
<p dir="ltr">
    <img
        src="https://lh6.googleusercontent.com/BdSFCpibt9IYfQLOdXWf9N6LhS-07HL3vJeXlqrwV4wTJWnrBn1y1g8N7ut-HkM7eBwxv1SxADfkTIeBiyKB6ff2OwnvvWIsAXIXpxH03Vzv9OWl1ZKSZlhDKHIqHWhHCXy2HWeo"
        width="602"
        height="235"
    />
</p>
<p dir="ltr">
    If the exception is encountered mean, the client is no longer connected
    then it is removed from the client’s list and the message then broadcasted.
</p>
<ol start="6">
    <li dir="ltr">
        <p dir="ltr">
            The module Recieve is executed when the server is started. It
            accepts the client’s connection and asks for the nickname. It is
            responsible for managing and executing all other modules and
            starting a new thread for the new client. It constantly executes
            while the server is up.
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh4.googleusercontent.com/oUIioLWGTldzUGCDW0anv-V6WVqhprR1vPgxJ-pTSg_jc2GN6krVQ7mhPW1Pm8M2rlU13weYh-T4faIheAfwVU1B1teaL2QooZBf-OJXE-vzNgFJ6ioRkDBCpvaF81Jkm7aIJGw5"
        width="602"
        height="444"
    />
</p>
<p dir="ltr">
    The client is being checked in the txt file, if he is banned then he is not
    allowed to enter the chatroom. if it is admin then the password is asked
    which on in correction, the client is removed due to encryption and wrong
    password to save privacy.
</p>
<ol start="7">
    <li dir="ltr">
        <p dir="ltr">
            Function kick_user
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh6.googleusercontent.com/e8f43cb1rrnLAhNTUnGvLLGsK8mjctXdFX2JPikPzgaNMoVtrysOwAfwP5KOER59IpjeetrLqMAcX6CHFAuZUbApWCUZYHvhvjSZbAyr4ZMe2wG6-WnM9soPfoKyPC4S5JnSTMq7"
        width="602"
        height="267"
    />
</p>
<p dir="ltr">
    Function kick_user gets the name parameter and then kicks the specific
    person the message broadcasted to all users.
</p>
<ul>
    <li dir="ltr">
        <h2 dir="ltr">
            2.2 Client Implementation:
        </h2>
    </li>
</ul>
<p dir="ltr">
    Procedure to Implement the Client Script:
</p>
<ol>
    <li dir="ltr">
        <p dir="ltr">
            Same as Server, the two libraries are imported, Socket and Thread.
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh3.googleusercontent.com/SuYwDVq2ZQi22OQDuiqtLkTL7f6pg8Kzra6hFmLuUkmaAaeVdaomlHZnT_ZKLE2Xkev4D04F41xpTd4yyviMCRqUJiwFNhu4BeeWN-5L9Cxmz1_hRm2ps-hKxUhq-ImNtT59Oorm"
        width="182"
        height="48"
    />
</p>
<ol start="2">
    <li dir="ltr">
        <p dir="ltr">
            The client is asked to enter the nickname which is then used as its
            identifier in the broadcasting messages and to the server.
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh3.googleusercontent.com/c0p3REHrO7MKyr5UkDPrOK5y_dNnwWwDfiOYiSfN5TiW88DgTlcRebPEPKOQYIAEy98Rmd2O_ft361xNNgSkX5BYebmcxs_G5E18WTv9_Bm3rkhpdmWE0Ie19yBx9v8_g3c5yEcf"
        width="602"
        height="192"
    />
</p>
<p dir="ltr">
    Nickname is checked on the client site if he is the admin, the password is
    pre-saved on the client site so it can be sent to the server. A thread_stop
    variable is made to be used later.
</p>
<p dir="ltr">
    The client’s socket is defined over the internet socket and TCP connection,
    Then the client is connected to the server via the server’s IP and port.
</p>
<br/>
<ol start="3">
    <li dir="ltr">
        <p dir="ltr">
            The receive module is generated to carry out the messages from the
            server. The messages encoded in ASCII are decoded into again its
            original type. If the message is NICK then the user has to give the
            nickname for identification purposes. Using the print the
            broadcasted messages are printed over the client’s screen which is
            from another client via server. If an exception occurred, the error
            will be shown.
            <img
                src="https://lh3.googleusercontent.com/XGVPcuZhwqysckD2gUXZCRLjmGmQh2z6gK4EClbwgYv6WBb6UWJUeAvNRc78BIZshjWyPe6K75xUwJt1c_m1I9No4a3DyPcxNXvAZO3HBhYTd3KyzhNRZVkB0vZ9wLNaUeZMEPoi"
                width="602"
                height="509"
            />
        </p>
    </li>
</ol>
<p dir="ltr">
    The above program also shows that, if the server asks for a pass then a
    pass must be provided by the client. An incorrect password means the client
    can’t log in.
</p>
<ol start="4">
    <li dir="ltr">
        <p dir="ltr">
            The module write is defined for the user to write messages to the
            server, then broadcast to the clients. Messages are encoded in
            ASCII so they can be sent in bytes.
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh6.googleusercontent.com/AbjfoDBAJ1JzARssJY8ls29c1P-SglKJS_AYQbgD86x1kt3rb0gn-4PGTIRIa2k96GsbjpWVkAs-BaXN8p1_pMzb2nNKQ1tGwUDc0pnUDNZouSGiAU-7WA-APcksuotg02EqtAMu"
        width="602"
        height="285"
    />
</p>
<p dir="ltr">
    Message is written by the user, if he is a admin then he can perform
    commands start with $ symbol , like kick and ban , as name ,:1 and space 1
    1+1=2 numbers so the $ must be at nickname+2 where $kick+space=6 and
    $ban+space=5.
</p>
<ol start="5">
    <li dir="ltr">
        <p dir="ltr">
            Two Threads are generated for write and receive messages, which is
            started by using start().
        </p>
    </li>
</ol>
<p dir="ltr">
    <img
        src="https://lh5.googleusercontent.com/63Gl0Q4W1YHg95RrwmahEeCvClrB-BGX2F6viBK4iN8e-XVHPCTwD1jhSYINbsB98PSuQLOz4ecMMY81iVIMMNN1vKQThZQ9oSYCLfPpqlkBCAGvs7Wg_lIhm-bkMA26Y4cVvL-j"
        width="602"
        height="127"
    />
</p>
<h2 dir="ltr">
    2.2 Implementation:
</h2>
<p dir="ltr">
    <img
        src="https://lh3.googleusercontent.com/PmSrpkj-4lx2qfDnyJ1kk4VQfeVHGgS6NBHIA1PQy1_eK-QE1l_GAsunp3bD0Zn5voJyU1UPkbZ7xBNNfl3MYuycUFhkFKIrt2PA9f9cq-YTHOO3GEVTrkh973SFVmRXgk46dkDB"
        width="602"
        height="479"
    />
</p>
<p dir="ltr">
    Here we can see the TCP chatroom is running with multiple clients (let’s
    consider two clients ), The client is named nickname Usama, and the other
    client is named nickname as F4LL when Usama wants to communicate to the
    F4ll, he writes the message which broadcasted via the server and seen on
    the client’s side.
</p>
<br/>
<p dir="ltr">
    While on the server’s side the client’s IP and port and his connected
    nickname which he wrote are seen. If any client leaves the chatroom, it
    displays the specific client left.
</p>
<p dir="ltr">
    So, it enables multiple clients to communicate with each other easily by
    connecting to the server.
</p>
<p dir="ltr">
    <img
        src="https://lh5.googleusercontent.com/oier_PcLWVX8H5XWaNX9U67GhsDhx4p-12_LO8PUDakoQSMxLvf95JH7AE07_Rmz8qFDBkLH5bBmalC6uzgzv_cO-ezN6v_sBLGCvs0SuNnDh3FsW3i-0QSIUm4FQE-Dq5ElFqa5"
        width="602"
        height="481"
    />
</p>
<br/>
<h2 dir="ltr">
    2.3 Ban and Kick Feature:
</h2>
<p dir="ltr">
    <img
        src="https://lh4.googleusercontent.com/iNWnK4UzOKcCuR1J6PSMzviLXQebujZT3RUgqtur-tfXnEJ_9BI5Bj_eYT_A95veSig9UCfcL3EFnS5bdp8e50LJzZ3-tYwsV6CgBQVPXjgFNHPDxNZTgJ44Pn6_u2J-UaD2pY1S"
        width="602"
        height="445"
    />
</p>
<p dir="ltr">
    In the above example, admin banned us and kicked noob , noob can reconnect
    but the us can’t. admin has the privilege. Admin is asked a password to
    enter but not the others.
</p>
<p dir="ltr">
    Ban.txt:
</p>
<p dir="ltr">
    It contains all the banned users. (For now, i haven’t added any encryption
    to this txt file as it is on the server pc and can’t be accessed by client)
</p>
<p dir="ltr">
    <img
        src="https://lh5.googleusercontent.com/0ZXe1qzBcBGceEG3foC5x2WG0qItLOybnpS1Bp2KzPQ6v6SK1lcFhBcvXVdNYE4QukcZVuW-qS61xkgnV_jd7LqKS9eStok2Mn4v0dnnD4bMYVSf0UhL6P0bl9yaHrkPFjoa6Bzp"
        width="602"
        height="527"
    />
</p>
<br/>
<h2 dir="ltr">
    For The Public Connection:
</h2>
<p dir="ltr">
    To implement the public connection, the port will need to be opened for the
    public. The port can be checked online if it is opened for the specific IP
    or not while some ports are reserved. The public IP can then be used to
    connect to the server.
</p>
<br/>
<h2 dir="ltr">
    TCP Chart:
</h2>
<p dir="ltr">
    <img
        src="https://lh6.googleusercontent.com/3AyZ3YSuz7DtruCbR_aVToyXwNqQWh56sw-dyy24sS7avK2i7mSm3mGYdr4ZROzWv3LsNliS64jUG0ABOFHdpCxHPEDnmpHDOGSxP2nbV1RdSjbT7sVgX8dLZ9NUFioJeob0nXaN"
        width="583"
        height="626"
    />
</p>
<br/>
<br/>
<br/>
<h1 dir="ltr">
    Conclusion:
</h1>
<p dir="ltr">
    At the very end, we have our awesome and lightweight TCP chat room running
    on full-efficient. This chatroom is efficient in terms of size and term of
    speed. The clients can be connected from different places by providing the
    server’s public IP and opening the port. In the example, we use the local
    hosts but can be implemented publicly.
</p>
<br/>
<p dir="ltr">
    This awesome TCP chat room ultimately enables you to communicate with your
    project members, school friends, office colleagues easily just by adjusting
    a host server.
</p>
<br/>
<h1 dir="ltr">
    Citation:
</h1>
<ul>
    <li dir="ltr">
        <p dir="ltr">
            <a
                href="https://en.wikipedia.org/wiki/Transmission_Control_Protocol"
            >
                https://en.wikipedia.org/wiki/Transmission_Control_Protocol
            </a>
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            <a
                href="https://en.wikipedia.org/wiki/Python_(programming_language)"
            >
                https://en.wikipedia.org/wiki/Python_(programming_language)
            </a>
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            <a href="http://docs.python.org/3/howto/sockets.html">
                http://docs.python.org/3/howto/sockets.html
            </a>
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            <a href="https://docs.python.org/3/library/threading.html">
                https://docs.python.org/3/library/threading.html
            </a>
        </p>
    </li>
    <li dir="ltr">
        <p dir="ltr">
            The Python Bible Volume 1: Python Programming For Beginners
            (Basics, Introduction) Kindle Edition
        </p>
    </li>
</ul>
<br/>
