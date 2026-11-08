import { useEffect, useMemo, useState } from "react";
import { Edit, Plus, RefreshCcw, Save, Trash2, X } from "lucide-react";
import AppLayout from "./AppLayout";
import { resourceApi } from "../services/api";

const emptyFromFields = (fields) =>
  fields.reduce((values, field) => ({ ...values, [field.name]: field.defaultValue || "" }), {});

function ManagementPage({
  user,
  currentPage,
  onNavigate,
  onLogout,
  title,
  subtitle,
  resource,
  fields,
  columns,
  extraActions,
}) {
  const api = useMemo(() => resourceApi(resource), [resource]);
  const [items, setItems] = useState([]);
  const [form, setForm] = useState(() => emptyFromFields(fields));
  const [editingId, setEditingId] = useState("");
  const [loading, setLoading] = useState(true);
  const [status, setStatus] = useState("");

  const loadItems = async () => {
    setLoading(true);
    try {
      setItems(await api.list());
      setStatus("");
    } catch (error) {
      setStatus(error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadItems();
  }, [api]);

  const updateField = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
  };

  const resetForm = () => {
    setForm(emptyFromFields(fields));
    setEditingId("");
  };

  const submitForm = async (event) => {
    event.preventDefault();
    try {
      if (editingId) {
        await api.update(editingId, form);
      } else {
        await api.create(form);
      }
      resetForm();
      await loadItems();
    } catch (error) {
      setStatus(error.message);
    }
  };

  const editItem = (item) => {
    setEditingId(item._id);
    setForm(
      fields.reduce(
        (values, field) => ({
          ...values,
          [field.name]:
            field.type === "date" && item[field.name]
              ? item[field.name].slice(0, 10)
              : item[field.name] ?? "",
        }),
        {}
      )
    );
  };

  const deleteItem = async (id) => {
    if (!window.confirm("Delete this record?")) return;
    try {
      await api.remove(id);
      await loadItems();
    } catch (error) {
      setStatus(error.message);
    }
  };

  return (
    <AppLayout user={user} currentPage={currentPage} onNavigate={onNavigate} onLogout={onLogout}>
      <section className="page-heading">
        <div>
          <h1>{title}</h1>
          <p>{subtitle}</p>
        </div>
        <button className="btn btn-outline-primary" onClick={loadItems} type="button">
          <RefreshCcw size={16} />
          Refresh
        </button>
      </section>

      <section className="management-grid">
        <form className="module-panel" onSubmit={submitForm}>
          <h2>{editingId ? "Update record" : "Add record"}</h2>
          <div className="form-grid">
            {fields.map((field) => (
              <label key={field.name} className={field.full ? "full" : ""}>
                <span>{field.label}</span>
                {field.type === "select" ? (
                  <select
                    className="form-select"
                    name={field.name}
                    value={form[field.name]}
                    onChange={updateField}
                    required={field.required}
                  >
                    <option value="">Choose</option>
                    {field.options.map((option) => (
                      <option key={option} value={option}>
                        {option}
                      </option>
                    ))}
                  </select>
                ) : field.type === "textarea" ? (
                  <textarea
                    className="form-control"
                    name={field.name}
                    value={form[field.name]}
                    onChange={updateField}
                    required={field.required}
                    rows="3"
                  />
                ) : (
                  <input
                    className="form-control"
                    type={field.type || "text"}
                    name={field.name}
                    value={form[field.name]}
                    onChange={updateField}
                    required={field.required}
                  />
                )}
              </label>
            ))}
          </div>

          {status && <p className="status-message error">{status}</p>}

          <div className="button-row">
            <button className="btn btn-primary" type="submit">
              {editingId ? <Save size={16} /> : <Plus size={16} />}
              {editingId ? "Save changes" : "Add"}
            </button>
            {editingId && (
              <button className="btn btn-light" type="button" onClick={resetForm}>
                <X size={16} />
                Cancel
              </button>
            )}
          </div>
        </form>

        <div className="module-panel table-panel">
          <h2>{title} List</h2>
          <div className="table-responsive">
            <table className="table align-middle">
              <thead>
                <tr>
                  {columns.map((column) => (
                    <th key={column.key}>{column.label}</th>
                  ))}
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {loading ? (
                  <tr>
                    <td colSpan={columns.length + 1}>Loading records...</td>
                  </tr>
                ) : items.length === 0 ? (
                  <tr>
                    <td colSpan={columns.length + 1}>No records yet.</td>
                  </tr>
                ) : (
                  items.map((item) => (
                    <tr key={item._id}>
                      {columns.map((column) => (
                        <td key={column.key}>
                          {column.render ? column.render(item) : item[column.key]}
                        </td>
                      ))}
                      <td>
                        <div className="table-actions">
                          {extraActions?.(item, loadItems)}
                          <button
                            className="btn btn-sm btn-light"
                            onClick={() => editItem(item)}
                            type="button"
                          >
                            <Edit size={15} />
                          </button>
                          <button
                            className="btn btn-sm btn-outline-danger"
                            onClick={() => deleteItem(item._id)}
                            type="button"
                          >
                            <Trash2 size={15} />
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </AppLayout>
  );
}

export default ManagementPage;
