import ManagementPage from "../components/ManagementPage";

const fields = [
  { name: "name", label: "Tenant Name", required: true },
  { name: "phone", label: "Phone", required: true },
  { name: "email", label: "Email", type: "email" },
  { name: "roomNumber", label: "Room Number", required: true },
  { name: "rentAmount", label: "Rent Amount", type: "number", required: true },
  { name: "moveInDate", label: "Move-in Date", type: "date" },
  {
    name: "status",
    label: "Status",
    type: "select",
    options: ["Active", "Notice", "Left"],
    defaultValue: "Active",
  },
  { name: "guardianName", label: "Guardian Name" },
  { name: "guardianPhone", label: "Guardian Phone" },
];

const columns = [
  { key: "name", label: "Tenant" },
  { key: "phone", label: "Phone" },
  { key: "roomNumber", label: "Room" },
  { key: "rentAmount", label: "Rent", render: (item) => `Rs ${item.rentAmount}` },
  { key: "status", label: "Status" },
];

function TenantManagement(props) {
  return (
    <ManagementPage
      {...props}
      title="Tenant Management"
      subtitle="Add, edit, delete, and view tenant records."
      resource="tenants"
      fields={fields}
      columns={columns}
    />
  );
}

export default TenantManagement;
