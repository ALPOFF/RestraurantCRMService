import DishesListItemComponent from '../DishesListItemComponent/DishesListItemComponent';

const DishesListComponent = () => {
	return (
		<div>
			Список блюд
			<div>
				<DishesListItemComponent />
				<div>
					<button>Добавить</button>
					<button>Удалить</button>
				</div>
			</div>
		</div>
	);
};

export default DishesListComponent;
