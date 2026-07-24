export default function ChatbotPreview() {
  return (
    <section className="py-24">

      <div className="max-w-6xl mx-auto px-6">

        <h2 className="text-center text-5xl font-bold">
          Meet Your AI Wellness Companion
        </h2>

        <div className="mt-16 rounded-3xl border bg-white dark:bg-slate-900 shadow-xl p-8">

          <div className="space-y-6">

            <div className="rounded-2xl bg-slate-100 p-4 w-fit">
              Hi, I've been feeling stressed lately.
            </div>

            <div className="ml-auto rounded-2xl bg-violet-600 text-white p-4 w-fit max-w-lg">
              I'm sorry you're feeling that way. Would you like to tell me what's been causing your stress? We can explore it together.
            </div>

          </div>

        </div>

      </div>

    </section>
  );
}