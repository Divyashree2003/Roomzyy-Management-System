import React from "react";
import {
  ArrowLeft,
  Bell,
  Settings,
  HelpCircle,
  Download,
  Mail,
  CheckCircle,
  Send,
} from "lucide-react";

export default function AlertDetails({
  onBack,
  onDashboard,
  onOpenMaintenance,
  onOpenStaffTools,
}) {
  return (
    <div className="flex h-screen bg-gray-100">

      {/* Sidebar */}
      <div className="w-64 bg-white shadow-lg flex flex-col justify-between">

        <div>

          <div className="p-6">
            <h1 className="text-2xl font-bold text-blue-700">
              PG Management
            </h1>

            <p className="text-gray-500 text-sm">
              Enterprise Management
            </p>
          </div>

          <nav className="mt-5">
            <ul className="space-y-2">

              <li
                className="px-6 py-3 hover:bg-gray-100 cursor-pointer"
                onClick={onDashboard}
              >
                Dashboard
              </li>

              <li
                className="px-6 py-3 bg-blue-50 border-r-4 border-blue-700 text-blue-700 font-semibold cursor-pointer"
                onClick={onBack}
              >
                Notifications
              </li>

              <li
                className="px-6 py-3 hover:bg-gray-100 cursor-pointer"
                onClick={onOpenMaintenance}
              >
                Maintenance
              </li>

              <li
                className="px-6 py-3 hover:bg-gray-100 cursor-pointer"
                onClick={onOpenStaffTools}
              >
                Staff Tools
              </li>

            </ul>
          </nav>

        </div>

        <div className="p-6 space-y-4">

          <div className="flex items-center gap-2 text-gray-600">
            <Settings size={18} />
            Settings
          </div>

          <div className="flex items-center gap-2 text-gray-600">
            <HelpCircle size={18} />
            Support
          </div>

        </div>

      </div>

      {/* Main Content */}
      <div className="flex-1 p-6 overflow-auto">

        {/* Header */}
        <div className="flex justify-between items-center mb-6">

          <div className="flex items-center gap-4">

            <button
              onClick={onBack}
              className="text-gray-700"
            >
              <ArrowLeft />
            </button>

            <h2 className="text-2xl font-bold text-gray-800">
              Alert Details
            </h2>

          </div>

          <div className="flex items-center gap-4">

            <input
              type="text"
              placeholder="Search invoices or tenants..."
              className="border px-4 py-2 rounded-xl w-80"
            />

            <Bell className="text-gray-600" />

            <img
              src="https://i.pravatar.cc/40"
              alt="profile"
              className="w-10 h-10 rounded-full"
            />

          </div>

        </div>

        {/* Alert Title */}
        <div className="flex justify-between items-center mb-6">

          <div>

            <span className="bg-red-100 text-red-600 px-3 py-1 rounded-full text-sm font-semibold">
              URGENT
            </span>

            <h1 className="text-4xl font-bold mt-3 text-gray-900">
              Rent Due: Unit 402
            </h1>

            <p className="text-gray-500 mt-2">
              Automated notification triggered for tenant.
            </p>

          </div>

          <div className="flex gap-3">

            <button className="border px-5 py-3 rounded-xl flex items-center gap-2">
              <Download size={18} />
              Download PDF
            </button>

            <button className="bg-blue-700 text-white px-5 py-3 rounded-xl flex items-center gap-2">
              <Mail size={18} />
              Contact Manager
            </button>

          </div>

        </div>

        {/* Layout */}
        <div className="grid grid-cols-3 gap-6">

          {/* Left Panel */}
          <div className="space-y-6">

            {/* Invoice Overview */}
            <div className="bg-white rounded-2xl shadow p-6 border-l-4 border-red-500">

              <h2 className="text-xl font-semibold mb-6">
                Invoice Overview
              </h2>

              <div className="space-y-5">

                <div className="flex justify-between">
                  <span className="text-gray-500">
                    Amount Due
                  </span>

                  <span className="font-bold text-2xl">
                    $2,450
                  </span>
                </div>

                <div className="flex justify-between">
                  <span className="text-gray-500">
                    Due Date
                  </span>

                  <span className="text-red-600 font-semibold">
                    Oct 05, 2023
                  </span>
                </div>

                <div className="flex justify-between">
                  <span className="text-gray-500">
                    Property
                  </span>

                  <span className="font-semibold">
                    Skyline Heights
                  </span>
                </div>

                <div className="flex justify-between">
                  <span className="text-gray-500">
                    Unit Number
                  </span>

                  <span className="font-semibold">
                    402-B
                  </span>
                </div>

              </div>

              {/* Alert Box */}
              <div className="mt-6 bg-gray-100 rounded-xl p-4 text-sm text-gray-600">
                Late fee will automatically apply if payment is not received.
              </div>

            </div>

            {/* Property Image */}
            <div className="bg-white rounded-2xl shadow overflow-hidden">

              <img
                src="https://images.unsplash.com/photo-1460317442991-0ec209397118?q=80&w=1200&auto=format&fit=crop"
                alt="building"
                className="h-64 w-full object-cover"
              />

              <div className="p-4">
                <h3 className="text-gray-500 text-sm">
                  PROPERTY LOCATION
                </h3>

                <p className="font-bold text-xl">
                  1200 Metropolitan Ave
                </p>
              </div>

            </div>

          </div>

          {/* Right Panel */}
          <div className="col-span-2 space-y-6">

            {/* Multi Channel Log */}
            <div className="bg-white rounded-2xl shadow p-6">

              <div className="flex justify-between items-center mb-5">

                <h2 className="text-xl font-semibold">
                  Multi-Channel Log
                </h2>

                <span className="text-green-600 font-semibold">
                  3/3 Delivered
                </span>

              </div>

              <div className="grid grid-cols-3 gap-4">

                <div className="border rounded-xl p-4">
                  <div className="flex justify-between">

                    <span>SMS</span>

                    <CheckCircle className="text-green-600" />
                  </div>

                  <p className="text-sm text-gray-500 mt-3">
                    Delivered successfully
                  </p>
                </div>

                <div className="border rounded-xl p-4">
                  <div className="flex justify-between">

                    <span>Email</span>

                    <CheckCircle className="text-green-600" />
                  </div>

                  <p className="text-sm text-gray-500 mt-3">
                    Opened by tenant
                  </p>
                </div>

                <div className="border rounded-xl p-4">
                  <div className="flex justify-between">

                    <span>Push</span>

                    <CheckCircle className="text-green-600" />
                  </div>

                  <p className="text-sm text-gray-500 mt-3">
                    Notification delivered
                  </p>
                </div>

              </div>

            </div>

            {/* Communication History */}
            <div className="bg-white rounded-2xl shadow p-6">

              <div className="flex justify-between items-center mb-6">

                <h2 className="text-xl font-semibold">
                  Communication History
                </h2>

                <button className="text-blue-700 text-sm">
                  View All
                </button>

              </div>

              <div className="space-y-5">

                {/* System */}
                <div className="bg-gray-100 rounded-xl p-4">
                  <h3 className="font-semibold">
                    System Automation
                  </h3>

                  <p className="text-gray-600 mt-2 text-sm">
                    Automated rent reminder notification sent.
                  </p>
                </div>

                {/* Manager */}
                <div className="bg-blue-700 text-white rounded-xl p-4">
                  <h3 className="font-semibold">
                    Manager Note
                  </h3>

                  <p className="mt-2 text-sm">
                    Tenant contacted personally regarding pending payment.
                  </p>
                </div>

                {/* Payment */}
                <div className="bg-gray-100 rounded-xl p-4">
                  <h3 className="font-semibold">
                    Payment Processor
                  </h3>

                  <p className="text-red-600 mt-2 text-sm">
                    Transaction Declined - Insufficient Funds
                  </p>
                </div>

              </div>

              {/* Message Box */}
              <div className="flex gap-3 mt-6">

                <input
                  type="text"
                  placeholder="Add note or message..."
                  className="flex-1 border rounded-xl px-4 py-3"
                />

                <button className="bg-blue-700 text-white px-6 rounded-xl flex items-center gap-2">
                  <Send size={18} />
                  Send
                </button>

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}
