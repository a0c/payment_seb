from openerp import models, fields


class SEBPaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    seb_PRIVATE_KEY = fields.Char('Private Key', size=256, help='Path to Private Key')
    seb_BANK_CERT = fields.Char('Bank Certificate', size=256, help='Path to Bank Certificate')

    def _get_providers(self, cr, uid, context=None):
        providers = super(SEBPaymentAcquirer, self)._get_providers(cr, uid, context=context)
        providers.append(['seb', 'SEB'])
        return providers

    def seb_form_generate_values(self, cr, uid, id, partner_values, tx_values, context=None):
        return self.banklink_form_generate_values(cr, uid, id, partner_values, tx_values, context=context)

    def seb_get_private_key(self):
        return self.seb_PRIVATE_KEY

    def seb_get_bank_cert(self):
        return self.seb_BANK_CERT

    def seb_get_form_action_url(self, cr, uid, id, context=None):
        env = self.read(cr, uid, id, ['environment'], context=context)['environment']
        return env == 'prod' and 'https://www.seb.ee/cgi-bin/unet3.sh/un3min.r' or 'http://localhost:3480/banklink/seb-common'
