from django.shortcuts import render

def index(request):
	return render(request, 'ninja/index.html')

def color(request, color):
	if color=='red':
		context={
			'name': 'Raphael',
			'img': 'ninja/red.gif',
		}
		return render(request, 'ninja/color.html', context)
		

	elif color=='orange':
		orange={
		'name': 'Michelangelo',
		'img': 'ninja/orange.jpg',
		}
		return render(request, 'ninja/color.html', orange)

	elif color=='purple':
		purple={
		'name': 'Donatello',
		'img': 'ninja/purple.png',
		}
		return render(request, 'ninja/color.html', purple)

	elif color=='blue':
		blue={
		'name': 'Leonardo',
		'img': 'ninja/blue.jpg',
		}
		return render(request, 'ninja/color.html', blue)

	else:
		megan={
		'name': 'Megan Fox',
		'img': 'ninja/mf.jpg',
		}
		return render(request, 'ninja/color.html', megan)