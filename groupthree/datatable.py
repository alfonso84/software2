#-*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.core.urlresolvers import reverse
from groupthree.models import Sala, Juego	


class SalaPublicaDatatableView(LoginRequiredMixin, BaseDatatableView):
	model = Sala
	columns = [
			'sala_id', 
			'juego', 
			'capacidad_maxima',
			'cantidad_usuarios',
			]
	order_columns = [
			'sala_id', 
			'juego', 
			'capacidad_maxima',
			'cantidad_usuarios',
			]
	max_display_length = 100


	def get_initial_queryset(self):
		queryset = Sala.objects.filter(es_publica=True)
		return queryset

	def prepare_results(self, queryset):
		data = []
		for item in queryset:
			sala_id = item.pk
			juego = item.juego.juego
			capacidad_maxima = item.capacidad_maxima
			cantidad_usuarios = item.cantidad_usuarios

			actions = ''
			html_action = '''<a href="%s" class="btn btn-default btn-xs" 
						data-toggle="tooltip" title="%s">
							<div class="text-danger">
								<i class="fa %s"></i>
							</div>
						</a>'''

			html_button = '''<button class="btn btn-default btn-xs" 
						data-toggle="tooltip" title="%s" 
						onclick="unirseSala(%s)" data-id="%s">
								<div class="text-danger">
									<i class="fa %s" style="margin-right: 3px;"></i>
								</div>
						</button>'''

			action_join = html_button % (
				'Unirse a la sala',
				item.pk,
					   				 item.pk,
					   				 'fa-magnet'
			)

			actions = action_join

			data.append([sala_id,juego,capacidad_maxima,cantidad_usuarios, actions])
		return data
