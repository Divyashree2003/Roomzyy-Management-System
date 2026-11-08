function StatCard({ label, value, detail, icon: Icon }) {
  return (
    <article className="stat-card">
      <div>
        <p>{label}</p>
        <strong>{value}</strong>
        {detail && <span>{detail}</span>}
      </div>
      {Icon && (
        <div className="stat-icon">
          <Icon size={22} />
        </div>
      )}
    </article>
  );
}

export default StatCard;
