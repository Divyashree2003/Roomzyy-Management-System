import ManagementPage from "../components/ManagementPage";

const fields = [
  { name: "tenantName", label: "Tenant Name", required: true },
  { name: "roomNumber", label: "Room Number", required: true },
  { name: "amount", label: "Amount", type: "number", required: true },
  { name: "month", label: "Month", required: true },
  { name: "dueDate", label: "Due Date", type: "date", required: true },
  { name: "paidOn", label: "Paid On", type: "date" },
  {
    name: "method",
    label: "Method",
    type: "select",
    options: ["Cash", "UPI", "Card", "Bank"],
    defaultValue: "UPI",
  },
  {
    name: "status",
    label: "Status",
    type: "select",
    options: ["Paid", "Pending", "Overdue"],
    defaultValue: "Pending",
  },
];

const columns = [
  { key: "tenantName", label: "Tenant" },
  { key: "roomNumber", label: "Room" },
  { key: "amount", label: "Amount", render: (item) => `Rs ${item.amount}` },
  { key: "month", label: "Month" },
  { key: "status", label: "Status" },
];

function PaymentManagement(props) {
  return (
    <ManagementPage
      {...props}
      title="Payment Management"
      subtitle="Collect rent, track payment history, and identify pending rent."
      resource="payments"
      fields={fields}
      columns={columns}
    />
  );
}

export default PaymentManagement;
