import os, uuid
from django.views.generic import TemplateView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image


class ImagesToPdfView(TemplateView):
    template_name = "images_to_pdf.html"

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist("images")
        context = {}

        if not files:
            context["error"] = "Please upload at least one image."
            return self.render_to_response(context)

        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, "uploads"))
        images = []

        for f in files:
            filename = fs.save(f"{uuid.uuid4()}_{f.name}", f)
            path = os.path.join(fs.location, filename)

            img = Image.open(path)

            # 🔥 Force convert to RGB to prevent corruption
            if img.mode != "RGB":
                img = img.convert("RGB")

            images.append(img)

        if not images:
            context["error"] = "No valid images to convert."
            return self.render_to_response(context)

        # 🔥 Save the PDF
        pdf_name = f"{uuid.uuid4()}_output.pdf"
        pdf_dir = os.path.join(settings.MEDIA_ROOT, "pdfs")
        os.makedirs(pdf_dir, exist_ok=True)
        pdf_path = os.path.join(pdf_dir, pdf_name)

        # First image saves the PDF, rest are appended
        first_img, *rest = images
        first_img.save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=rest)

        context["pdf_url"] = settings.MEDIA_URL + "pdfs/" + pdf_name
        return self.render_to_response(context)


class DashboardView(TemplateView):
    template_name = "dashboard.html"