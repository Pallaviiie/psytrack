export default function FAQ() {
  const faqs = [
    {
      q: "Is PsyTrack free to use?",
      a: "Yes. The basic features are completely free.",
    },
    {
      q: "Is my data secure?",
      a: "Yes. Your information is securely stored and protected.",
    },
    {
      q: "Can AI diagnose mental illness?",
      a: "No. PsyTrack provides support and screening, not a medical diagnosis.",
    },
  ];

  return (
    <section id="faq" className="py-24">

      <div className="max-w-4xl mx-auto px-6">

        <h2 className="text-5xl font-bold text-center">
          Frequently Asked Questions
        </h2>

        <div className="mt-16 space-y-6">

          {faqs.map((faq) => (
            <div
              key={faq.q}
              className="rounded-2xl border p-6"
            >
              <h3 className="font-bold text-xl">
                {faq.q}
              </h3>

              <p className="mt-3 text-slate-500">
                {faq.a}
              </p>

            </div>
          ))}

        </div>

      </div>

    </section>
  );
}