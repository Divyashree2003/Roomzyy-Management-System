# PG Management System

Complete MERN-style PG Management System with React + Vite frontend, Express backend, MongoDB/Mongoose data models, JWT authentication, and localStorage session persistence.

## Project Structure

```text
frontend/
  src/
    components/
    pages/
    services/
  package.json

backend/
  config/
  controllers/
  middleware/
  models/
  routes/
  package.json
  server.js
```

## Setup

1. Install MongoDB and keep it running locally, or prepare a MongoDB Atlas connection string.

2. Create `backend/.env`.

```env
PORT=5000
MONGO_URI=mongodb://127.0.0.1:27017/pg_management_system
JWT_SECRET=change_this_secret
CLIENT_URL=http://localhost:5173
```

3. Install backend dependencies.

```bash
cd backend
npm install
npm run dev
```

4. Install frontend dependencies.

```bash
cd frontend
npm install
npm run dev
```

5. Open the frontend URL shown by Vite, usually:

```text
http://localhost:5173
```

## Login Name Requirement

Registration sends `fullName` to `/api/auth/register`. The backend stores it as `User.name` in MongoDB. Login returns:

```json
{
  "token": "...",
  "user": {
    "id": "...",
    "name": "Divyashree",
    "email": "divya@example.com",
    "role": "Admin"
  }
}
```

The frontend stores that user in localStorage and the dashboard renders:

```text
Welcome Back, Divyashree 👋
```

## API Modules

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `GET/POST/PUT/DELETE /api/tenants`
- `GET/POST/PUT/DELETE /api/rooms`
- `GET/POST/PUT/DELETE /api/payments`
- `GET/POST/PUT/DELETE /api/visitors`
- `PATCH /api/visitors/:id/exit`
- `GET/POST /api/notifications`
- `POST /api/notifications/alerts`
- `PATCH /api/notifications/:kind/:id/read`
- `GET/POST/PUT/DELETE /api/maintenance`
- `PATCH /api/maintenance/:id/resolve`
- `GET/POST/PUT/DELETE /api/broadcasts`
