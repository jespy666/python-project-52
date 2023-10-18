from .test_setup import LabelTestCase


class TestLabelView(LabelTestCase):

    def test_success_view(self):
        response = self.client.get(self.labels_url)
        self.assertEqual(response.status_code, 302)