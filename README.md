 Roomzyy – PG Management System

A web-based Paying Guest (PG) Management System developed using the **MERN Stack** to simplify and organize PG operations. The application helps administrators manage tenants, rooms, rent payments, staff, visitors, utility expenses, maintenance, notifications and reports through a centralized platform.

 Project Overview

Managing a PG accommodation manually can be time-consuming and difficult. Roomzyy provides a centralized web application to improve the management of daily PG activities, reduce manual work and maintain organized records.

Objectives

- Simplify PG administration and daily operations.
- Manage tenant information and room allocation.
- Track rent payments and payment records.
- Organize staff and visitor management.
- Manage utility expenses and maintenance requests.
- Provide notifications and reports for better monitoring.

 Main Features

 1. Admin Module
- Dashboard and management overview.
- Tenant registration and verification.
- Room creation, allocation and management.
- Rent and payment tracking.
- Staff management.
- Visitor monitoring.
- Utility bill and expense management.
- Reports and analytics.
- Notifications and maintenance monitoring.

2. Staff Module
- Staff-related management activities.
- Visitor registration and entry/exit tracking.
- Maintenance and assigned task management.
- Relevant notifications.

 3. Tenant Module
- Tenant profile and information.
- Room details.
- Rent payment records.
- Visitor requests and QR-based passes.
- Maintenance complaints.
- Notifications.

 Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React.js, Vite, HTML, CSS, JavaScript |
| Backend | Node.js, Express.js |
| Database | MongoDB, Mongoose |
| Authentication | JWT |
| Development Tools | VS Code, Git, GitHub |
| API | REST API |

Project Structure

```text
Roomzyy-Management-System/
│
├── backend/
│   ├── config/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── package.json
│   └── server.js
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── package.json
│
├── docs/
├── scripts/
├── package.json
├── package-lock.json
├── .gitignore
└── README.md
```

 Installation and Setup

Prerequisites

- Node.js and npm
- MongoDB or MongoDB Atlas
- Git

 Step 1: Clone the Repository

```bash
git clone https://github.com/Divyashree2003/Roomzyy-Management-System.git
cd Roomzyy-Management-System
```

 Step 2: Configure Backend

Create a `.env` file inside the `backend` folder.

```env
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secure_secret
CLIENT_URL=http://localhost:5173
```

Use your own MongoDB connection string and a secure JWT secret. Never upload your `.env` file.

Install and start the backend:

```bash
cd backend
npm install
npm run dev
```

 Step 3: Configure Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Step 4: Open the Application

Open the local URL displayed by Vite, usually:

```text
http://localhost:5173
```

 Backend API Modules

- Authentication – Register, login and current-user details.
- Tenants – Tenant management.
- Rooms – Room management.
- Payments – Payment records.
- Visitors – Visitor registration and exit tracking.
- Notifications – Notifications and alerts.
- Maintenance – Maintenance requests and resolution.
- Broadcasts – Announcement management.

 Security

- JWT-based authentication.
- Role-based access control.
- Protected backend routes.
- Environment-based configuration for sensitive values.

Future Enhancements

- Online payment gateway integration improvements.
- Automated email and SMS notifications.
- Mobile application integration.
- Advanced analytics and dashboard improvements.
- Additional security and performance enhancements.

 Project Information

Project Name: Roomzyy – PG Management System  
Project Type:MCA Academic Project  
Architecture: MERN Stack Web Application  
Developer: Divyashree

GitHub Repository

[Roomzyy – PG Management System](https://github.com/Divyashree2003/Roomzyy-Management-System)

---

⭐ If you find this project interesting, feel free to explore the repository.
