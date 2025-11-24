// app/camera/page.tsx
export default function CameraPage() {
  return (
    <main className="min-h-screen bg-background flex flex-col items-center justify-center p-6">
      <h1 className="text-2xl font-bold mb-4">Raspberry Pi Camera</h1>
      <img
        src="py/stream"    // points to public/test.jpg
        alt="Raspberry Pi"
        className="w-2/3 rounded shadow-lg"
      />
    </main>
  );
}
