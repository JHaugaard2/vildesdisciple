export default function CameraStream() {
  return (
    <div className="w-full flex justify-center">
      <img
        src="https://vildesdisciple.com:8000/stream"
        alt="Live camera"
        className="rounded-lg shadow-lg border"
        style={{ maxWidth: "100%" }}
      />
    </div>
  );
}
