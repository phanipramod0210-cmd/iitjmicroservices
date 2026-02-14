# iitjmicroservices
IITJ Microservices Virtualbox VM project

# Microservices Deployment Using VirtualBox

## 📌 Project Objective
The objective of this project is to create and configure multiple Virtual Machines (VMs) using **Oracle VirtualBox**, establish networking between them, and deploy a **microservice-based application** across the connected VMs using Python-based REST services.

---

## 🧱 Project Architecture
The project consists of **three Virtual Machines**, each assigned a specific role:

1. **User Service VM**
   - Hosts a REST API for user data
   - Runs on port **8001**

2. **Order Service VM**
   - Hosts a REST API for order data
   - Runs on port **8002**

3. **API Gateway VM**
   - Acts as a single entry point for clients
   - Routes requests to User and Order services
   - Runs on port **8000**

---

## 🌐 Network Configuration
- All VMs are connected using **Host-Only Adapter**
- Each VM has a private IP address in the `192.168.56.0/24` network
- Services communicate using internal IPs

---

## 🛠 Technologies Used
- Oracle VirtualBox
- Ubuntu 24.04 LTS
- Python 3
- HTTPServer (`http.server`)
- REST API (GET endpoints)

---

## 📁 Project Folder Structure

microservices-project/ │ ├── user_service/ │   └── service.py │ ├── order_service/ │   └── service.py │ ├── gateway/ │   └── gateway.py │ └── README.md

---

## 🚀 Microservices Details

### 👤 User Service
- Endpoint: `/users`
- Port: `8001`
- Sample Response:
```json
{
  "users": ["Sumit", "Ved"]
}

📦 Order Service
Endpoint: /orders
Port: 8002
Sample Response:

{
  "orders": ["Order-101", "Order-102"]
}

🔀 API Gateway
Routes requests to appropriate microservices
Endpoints:
/users → User Service
/orders → Order Service
Port: 8000
▶️ How to Run the Project
Step 1: Start User Service

cd user_service
python3 service.py

Step 2: Start Order Service
cd order_service
python3 service.py

Step 3: Start API Gateway
cd gateway
python3 gateway.py

🧪 Testing the Application
curl http://<GATEWAY_VM_IP>:8000/users
curl http://<GATEWAY_VM_IP>:8000/orders

Or access via browser:
http://<GATEWAY_VM_IP>:8000/users
http://<GATEWAY_VM_IP>:8000/orders

🔹 Network Configuration to Connect Virtual Machines
Objective
To enable communication between multiple virtual machines hosting different microservices using a private and secure network.
Network Type Used: Host-Only Adapter
Why Host-Only Adapter?
Allows VM-to-VM communication
Allows Host-to-VM access (for browser/curl testing)
Blocks external internet access (secure & isolated)
Commonly recommended for academic microservice labs
Step-by-Step Network Configuration (VirtualBox)
Step 1: Open VirtualBox
Select a virtual machine
Click Settings → Network
Step 2: Configure Adapter
For each VM (User, Order, Gateway):
Adapter 1:
✅ Enable Network Adapter
Attached to: Host-only Adapter
Name: VirtualBox Host-Only Ethernet Adapter
Promiscuous Mode: Deny
Cable Connected: ✔
Click OK
Step 3: Verify IP Address Inside VM
Run the following command inside each VM:
Copy code
Bash
ip a
Each VM receives an IP like:
User Service VM → 192.168.56.101
Order Service VM → 192.168.56.102
API Gateway VM → 192.168.56.103
All VMs are now on the same private subnet.
Step 4: Test Connectivity
From one VM:
Copy code
Bash
ping 192.168.56.102
ping 192.168.56.103
✔ Successful ping confirms network connectivity.
Ports Used
Service
VM IP
Port
User Service
192.168.56.101
8001
Order Service
192.168.56.102
8002
API Gateway
192.168.56.103
8000
🔹 Architecture Design
Architecture Overview
This project follows a Microservices Architecture with an API Gateway pattern.
Each microservice runs independently on its own VM
Services communicate over HTTP
The API Gateway acts as a centralized entry point
Architecture Components
1️⃣ User Service
Runs on VM-1
Endpoint: /users
Port: 8001
Returns user data in JSON format
2️⃣ Order Service
Runs on VM-2
Endpoint: /orders
Port: 8002
Returns order data in JSON format
3️⃣ API Gateway
Runs on VM-3
Port: 8000
Routes requests:
/users → User Service
/orders → Order Service

Client (Browser / Curl)
        |
        v
+---------------------+
|     API Gateway     |
|   (Port: 8000)      |
| 192.168.56.103      |
+----------+----------+
           |
    -------------------
    |                 |
    v                 v
+-----------+   +------------+
| User VM   |   | Order VM   |
| Port 8001 |   | Port 8002  |
| /users    |   | /orders   |
| 192.168.56.101 | 192.168.56.102 |
+-----------+   +------------+

Architecture Benefits
🔹 Loose coupling between services
🔹 Independent deployment
🔹 Easy scalability
🔹 Centralized request handling
🔹 Clear separation of responsibilities





