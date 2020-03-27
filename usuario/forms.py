from django import forms
from usuario.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario

        fields = [
            'nombre',
            'dni',
            'fecha',
            'cuil',
            'tipo',
            'categoria',
            'cbu',
            'tel',
        ]

        labels = {
            'nombre':'Nombre y apellido',
            'dni':'DNI',
            'fecha':'Fecha de nacimineto',
            'cuil':'Cuil',
            'tipo':'Tipo',
            'categoria':'Categoria',
            'cbu':'CBU',
            'tel':'Tel',
        }
        TIPO = (
            ('Trabajador Informal', 'Trabajador Informal'),
            ('Monotributista', 'Monotributista'),
        )
        CATEGORIA = (
            ('Ninguna', 'Ninguna'),
            ('A', 'A'),
            ('B', 'B'),
        )

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'cuil': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(choices=TIPO,attrs={'class':'form-control'}),
            'categoria': forms.Select(choices=CATEGORIA,attrs={'class':'form-control'}),
            'cbu': forms.TextInput(attrs={'class':'form-control'}),
            'tel': forms.TextInput(attrs={'class':'form-control'}),
        }

class CargaForm(forms.ModelForm):
    class Meta:
        model=Usuario

        fields = [
            'estado',
            'observacion',
        ]

        labels = {
            'estado':'Carga',
            'observacion':'Observación',
        }

        widgets = {
            'estado':forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'observacion':forms.Textarea(attrs={'class':'form-control'}),
        }