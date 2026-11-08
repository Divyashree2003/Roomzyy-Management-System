import ManagementPage from "../components/ManagementPage";

const fields = [
  { name: "title", label: "Title", required: true },
  {
    name: "audience",
    label: "Audience",
    type: "select",
    options: ["All", "Staff", "Tenants"],
    defaultValue: "All",
  },
  {
    name: "priority",
    label: "Priority",
    type: "select",
    options: ["Normal", "Emergency"],
    defaultValue: "Normal",
  },
  { name: "message", label: "Message", type: "textarea", required: true, full: true },
];

const columns = [
  { key: "title", label: "Announcement" },
  { key: "audience", label: "Audience" },
  { key: "priority", label: "Priority" },
  { key: "message", label: "Message" },
];

function StaffBroadcastTool(props) {
  return (
    <ManagementPage
      {...props}
      title="Staff Broadcast"
      subtitle="Send announcements, emergency alerts, and review broadcast history."
      resource="broadcasts"
      fields={fields}
      columns={columns}
    />
  );
}

export default StaffBroadcastTool;
